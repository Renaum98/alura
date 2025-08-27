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


def extrair_numero_nota(texto: str):
    """Tenta extrair o número da nota fiscal a partir do texto."""
    texto = limpar_texto(texto).upper()

    if "RPS" in texto:
        return None

    # Regex expandida para capturar variações
    pattern = re.compile(
        r'(?:NOTA\s*FISCAL(?:\s*ELETR[ÔO]NICA)?|'
        r'NOTA\s*ELETR[ÔO]NICA\s*N[ºO]?|'
        r'NF(?:-E)?|'
        r'N[ºO])'
        r'(?:\s*[.:\-–]?\s*|\n\s*)'
        r'([\d.\s]{3,15})',
        re.IGNORECASE | re.DOTALL,
    )

    match = pattern.search(texto)
    if match:
        numero = re.sub(r'\D', '', match.group(1))  # remove pontos/espaços
        if numero and len(numero) >= 2:
            numero_int = int(numero)
            if numero_int > 0:
                return str(numero_int)
    return None


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


def gerar_nome_nao_encontrado(pasta, original_nome):
    """Gera nome único para notas não encontradas."""
    base = "nf_nao_encontrada"
    ext = ".pdf"
    contador = 1
    nome = f"{base}{ext}"
    while os.path.exists(os.path.join(pasta, nome)):
        nome = f"{base}_{contador}{ext}"
        contador += 1
    return nome


def processar_pdf(pdf_path: str):
    """Processa PDF e retorna número da NF se encontrado, caso contrário None."""
    texto = extrair_texto(pdf_path)
    return extrair_numero_nota(texto)


# -------------------------
# Interface Tkinter
# -------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Renomeador de Notas Fiscais")
        self.root.geometry("700x500")

        self.pasta = ""

        # Botões
        self.btn_select = ttk.Button(root, text="Selecionar Pasta", command=self.selecionar_pasta)
        self.btn_select.pack(pady=10)

        self.btn_start = ttk.Button(root, text="Iniciar Processamento", command=self.start_process)
        self.btn_start.pack(pady=10)

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

        threading.Thread(target=self.renomear_pdfs_na_pasta).start()

    def renomear_pdfs_na_pasta(self):
        """Processa e renomeia PDFs conforme regra."""
        arquivos = [f for f in os.listdir(self.pasta) if f.lower().endswith(".pdf")]
        log_path = os.path.join(self.pasta, "resultado.csv")

        total = len(arquivos)
        self.progress["maximum"] = total
        self.progress["value"] = 0

        with open(log_path, mode="w", newline="", encoding="utf-8") as log_file:
            writer = csv.writer(log_file, delimiter=";")
            writer.writerow(["Arquivo Original", "Novo Nome", "Status"])

            for arquivo in arquivos:
                caminho_original = os.path.join(self.pasta, arquivo)
                self.log(f"📂 Processando: {arquivo}")

                numero_nota = processar_pdf(caminho_original)

                if numero_nota:
                    # Encontrou NF → mantém nome original
                    self.log(f"✅ Número encontrado ({numero_nota}) → Mantendo nome: {arquivo}")
                    writer.writerow([arquivo, arquivo, "OK"])
                else:
                    # Não encontrou → renomeia
                    self.log(f"⚠️ Número da nota NÃO encontrado em: {arquivo}")
                    novo_nome = gerar_nome_nao_encontrado(self.pasta, arquivo)
                    caminho_novo = os.path.join(self.pasta, novo_nome)

                    if os.path.exists(caminho_novo):
                        self.log(f"⚠️ Arquivo {novo_nome} já existe. Pulando.")
                        writer.writerow([arquivo, novo_nome, "DUPLICADO"])
                    else:
                        shutil.move(caminho_original, caminho_novo)
                        self.log(f"📄 Renomeado para: {novo_nome}")
                        writer.writerow([arquivo, novo_nome, "NAO_ENCONTRADO"])

                # Atualiza barra de progresso sem travar GUI
                self.progress.after(10, self.progress.step, 1)

        self.log(f"\n📑 Log salvo em: {log_path}")
        messagebox.showinfo("Concluído", "Processamento finalizado!")


# -------------------------
# Execução
# -------------------------
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
