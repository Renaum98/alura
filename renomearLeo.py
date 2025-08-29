import os
import re
import pytesseract
import fitz  # PyMuPDF
from pdf2image import convert_from_path
from tkinter import filedialog, Tk, ttk, scrolledtext, messagebox
import shutil
import unicodedata
from PIL import Image, ImageEnhance, ImageFilter
import csv
import threading

# Configuração do caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Caminho para a pasta bin do Poppler (ajuste conforme onde extraiu)
POPPLER_PATH = r"C:\Users\user\Downloads\poppler-25.07.0\Library\bin"


# -------------------------
# Funções utilitárias
# -------------------------
def limpar_texto(texto: str) -> str:
    """Normaliza e limpa o texto extraído do PDF/OCR."""
    texto = unicodedata.normalize('NFKD', texto)
    texto = re.sub(r'\s+', ' ', texto)
    texto = texto.replace('\x0c', '')
    return texto.strip()


def extrair_estado_e_numero_nota(texto: str):
    """Extrai UF (estado válido do Brasil) e número da nota fiscal do texto."""
    texto = limpar_texto(texto).upper()

    # -------------------------
    # Número da nota
    # -------------------------
    pattern_numero = re.compile(
        r'(?:NOTA\s*FISCAL(?:\s*ELETR[ÔO]NICA)?|'
        r'NOTA\s*ELETR[ÔO]NICA\s*N[ºO]?|'
        r'NF(?:-E)?|'
        r'N[ºO])'
        r'(?:\s*[.:\-–]?\s*|\n\s*)'
        r'([\d.\s]{3,15})',
        re.IGNORECASE | re.DOTALL,
    )

    numero = None
    match = pattern_numero.search(texto)
    if match:
        numero = re.sub(r'\D', '', match.group(1))  # apenas dígitos
        if numero:
            numero = numero.lstrip("0")  # remove zeros à esquerda
            if len(numero) > 6:          # limita a 6 caracteres
                numero = numero[-6:]

    # -------------------------
    # UF (estado)
    # -------------------------
    ufs_validas = {
        "AC","AL","AM","BA","CE","DF","ES","GO","MA",
        "MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN",
        "RS","RO","RR","SC","SP","SE","TO"
    }

    uf = None
    # Captura "UF PI", "UF: PI", "UF\nPI"
    match_uf = re.search(r"UF[\s:\-]*([A-Z]{2})", texto, re.MULTILINE)
    if match_uf and match_uf.group(1) in ufs_validas:
        uf = match_uf.group(1)

    if uf and numero:
        return uf, numero
    return None, None




def melhorar_imagem(img):
    """Aplica filtros para melhorar qualidade do OCR."""
    img = img.convert('L')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.filter(ImageFilter.MedianFilter(3))
    img = img.point(lambda p: 255 if p > 128 else 0)
    return img


def extrair_texto(pdf_path: str) -> str:
    """Extrai texto de um PDF usando PyMuPDF e fallback com OCR (Tesseract)."""
    texto_extraido = ""

    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            texto_extraido += page.get_text()
        doc.close()

        if texto_extraido.strip():
            return texto_extraido
    except Exception as e:
        print(f"Erro ao extrair texto com PyMuPDF em {pdf_path}: {e}")

    try:
        imagens = convert_from_path(pdf_path, dpi=300, poppler_path=POPPLER_PATH)

        for img in imagens:
            img = melhorar_imagem(img)
            texto_extraido += pytesseract.image_to_string(img, lang="por")
    except Exception as e:
        print(f"OCR falhou para {pdf_path}: {e}")

    return texto_extraido


def gerar_nome_nao_encontrado(pasta):
    """Gera nome único para notas não encontradas."""
    base = "nf_nao_encontrada"
    ext = ".pdf"
    contador = 0
    while True:
        nome = f"{base}{'_' + str(contador) if contador > 0 else ''}{ext}"
        if not os.path.exists(os.path.join(pasta, nome)):
            return nome
        contador += 1


def processar_pdf(pdf_path: str):
    """Processa PDF e retorna UF + número da NF."""
    texto = extrair_texto(pdf_path)
    return extrair_estado_e_numero_nota(texto)


# -------------------------
# Interface Tkinter
# -------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Renomeador de Notas Fiscais")
        self.root.geometry("700x550")

        self.pasta = ""
        self.pause_event = threading.Event()
        self.pause_event.set()  # começa liberado

        # Botões
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)

        self.btn_select = ttk.Button(btn_frame, text="Selecionar Pasta", command=self.selecionar_pasta)
        self.btn_select.pack(side="left", padx=5)

        self.btn_start = ttk.Button(btn_frame, text="Iniciar Processamento", command=self.start_process)
        self.btn_start.pack(side="left", padx=5)

        self.btn_pause = ttk.Button(btn_frame, text="⏸️ Pausar", command=self.pause_process, state="disabled")
        self.btn_pause.pack(side="left", padx=5)

        self.btn_resume = ttk.Button(btn_frame, text="▶️ Continuar", command=self.resume_process, state="disabled")
        self.btn_resume.pack(side="left", padx=5)

        # Barra de progresso
        self.progress = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(pady=10)

        # Área de log
        self.log_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.log_area.pack(pady=10)

    def log(self, msg):
        """Mostra mensagem na área de log."""
        self.log_area.insert("end", msg + "\n")
        self.log_area.see("end")
        self.root.update_idletasks()

    def selecionar_pasta(self):
        """Abre diálogo para selecionar pasta."""
        pasta = filedialog.askdirectory(title="Selecione a pasta com os PDFs")
        if pasta:
            self.pasta = pasta
            self.log(f"📂 Pasta selecionada: {pasta}")

    def start_process(self):
        """Inicia processamento em thread separada para não travar GUI."""
        if not self.pasta:
            messagebox.showwarning("Aviso", "Selecione uma pasta primeiro.")
            return

        self.btn_pause["state"] = "normal"
        self.btn_resume["state"] = "disabled"

        threading.Thread(target=self.renomear_pdfs_na_pasta, daemon=True).start()

    def pause_process(self):
        """Pausa o processamento."""
        self.pause_event.clear()
        self.btn_pause["state"] = "disabled"
        self.btn_resume["state"] = "normal"
        self.log("⏸️ Processamento pausado...")

    def resume_process(self):
        """Continua o processamento."""
        self.pause_event.set()
        self.btn_pause["state"] = "normal"
        self.btn_resume["state"] = "disabled"
        self.log("▶️ Processamento retomado...")

    def renomear_pdfs_na_pasta(self):
        """Processa e renomeia PDFs conforme regra."""
        arquivos = [f for f in os.listdir(self.pasta) if f.lower().endswith(".pdf")]

        # Criar pasta "renomeados" dentro da escolhida
        pasta_destino = os.path.join(self.pasta, "renomeados")
        os.makedirs(pasta_destino, exist_ok=True)

        log_path = os.path.join(pasta_destino, "resultado.csv")

        total = len(arquivos)
        self.progress["maximum"] = total
        self.progress["value"] = 0

        with open(log_path, mode="w", newline="", encoding="utf-8") as log_file:
            writer = csv.writer(log_file, delimiter=";")
            writer.writerow(["Arquivo Original", "Novo Nome", "Status"])

            for arquivo in arquivos:
                self.pause_event.wait()  # respeita pausa

                caminho_original = os.path.join(self.pasta, arquivo)
                self.log(f"📂 Processando: {arquivo}")

                uf, numero_nota = processar_pdf(caminho_original)

                if uf and numero_nota:
                    # Nome no formato: UF NUMERO.pdf
                    novo_nome = f"{uf} {numero_nota}.pdf"
                    caminho_novo = os.path.join(pasta_destino, novo_nome)

                    if os.path.exists(caminho_novo):
                        self.log(f"⚠️ Arquivo {novo_nome} já existe. Pulando.")
                        writer.writerow([arquivo, novo_nome, "DUPLICADO"])
                    else:
                        shutil.copy(caminho_original, caminho_novo)  # mantém original
                        self.log(f"✅ NF encontrada ({uf} {numero_nota}) → Copiado para: {novo_nome}")
                        writer.writerow([arquivo, novo_nome, "OK"])
                else:
                    # Não encontrou → renomeia para nf_nao_encontrada
                    novo_nome = gerar_nome_nao_encontrado(pasta_destino)
                    caminho_novo = os.path.join(pasta_destino, novo_nome)

                    shutil.copy(caminho_original, caminho_novo)  # mantém original
                    self.log(f"⚠️ UF/Nota NÃO encontrada em: {arquivo}")
                    self.log(f"📄 Copiado como: {novo_nome}")
                    writer.writerow([arquivo, novo_nome, "NAO_ENCONTRADO"])

                # Atualiza barra de progresso
                self.progress["value"] += 1
                self.root.update_idletasks()

        self.log(f"\n📑 Log salvo em: {log_path}")
        messagebox.showinfo("Concluído", "Processamento finalizado!")
        self.btn_pause["state"] = "disabled"
        self.btn_resume["state"] = "disabled"


# -------------------------
# Execução
# -------------------------
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
