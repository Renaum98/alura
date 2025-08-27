import os
import re
import pytesseract
import fitz  # PyMuPDF
from pdf2image import convert_from_path
from tkinter import filedialog, Tk
import shutil
import unicodedata
from PIL import Image, ImageEnhance, ImageFilter

# Configuração do caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Caminho para a pasta bin do Poppler (ajuste conforme onde extraiu)
POPPLER_PATH = r"C:\Users\user\Downloads\poppler-25.07.0\Library\bin"

# --------------------------------------------
# Funções utilitárias
# --------------------------------------------

def selecionar_pasta():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Selecione a pasta com os PDFs")

def limpar_texto(texto):
    texto = unicodedata.normalize('NFKD', texto)
    texto = re.sub(r'\s+', ' ', texto)
    texto = texto.replace('\x0c', '')
    return texto.strip()

# --------------------------------------------
# OCR e extração de texto
# --------------------------------------------

def melhorar_imagem(img):
    img = img.convert('L')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.filter(ImageFilter.MedianFilter(3))
    img = img.point(lambda p: 255 if p > 128 else 0)
    return img

def extrair_texto(pdf_path):
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
        imagens = convert_from_path(pdf_path, dpi=600, poppler_path=POPPLER_PATH)

        for img in imagens:
            img = melhorar_imagem(img)
            texto_extraido += pytesseract.image_to_string(img, lang='por')
    except Exception as e:
        print(f"OCR falhou para {pdf_path}: {e}")

    return texto_extraido

# --------------------------------------------
# Extração do número da NF
# --------------------------------------------

def extrair_numero_nota(texto):
    texto = limpar_texto(texto).upper()

    if "RPS" in texto:
        return None

    # Aceita números simples (123456) ou formatados (000.000.123)
    pattern = re.compile(
        r'(?:NOTA\s*FISCAL(?:\s*ELETR[ÔO]NICA)?|NOTA\s*ELETR[ÔO]NICA\s*N[ºO]?|NF(?:-E)?|N[ºO])'
        r'(?:\s*[.:\-–]?\s*|\n\s*)([\d.\s]{3,15})',
        re.IGNORECASE | re.DOTALL
    )

    match = pattern.search(texto)
    if match:
        numero = re.sub(r'\D', '', match.group(1))  # remove pontos/espacos
        if numero:
            if len(numero) < 2:
                return None
            numero_int = int(numero)
            if numero_int > 0:
                return str(numero_int)
    return None

# --------------------------------------------
# Processamento dos PDFs
# --------------------------------------------

def processar_pdf(pdf_path):
    texto = extrair_texto(pdf_path)
    numero_nota = extrair_numero_nota(texto)
    return numero_nota

# --------------------------------------------
# Manipulação de arquivos
# --------------------------------------------

def gerar_nome_nao_encontrado(pasta):
    base = "nao encontrado"
    ext = ".pdf"
    contador = 1
    nome = base + ext
    while os.path.exists(os.path.join(pasta, nome)):
        nome = f"{base}_{contador}{ext}"
        contador += 1
    return nome

def renomear_pdfs_na_pasta(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")]

    for arquivo in arquivos:
        caminho_original = os.path.join(pasta, arquivo)
        print(f"\n📂 Processando: {arquivo}")

        numero_nota = processar_pdf(caminho_original)

        if numero_nota:
            novo_nome = f"{numero_nota}.pdf"
        else:
            print(f"⚠️ Número da nota não encontrado em: {arquivo}")
            novo_nome = gerar_nome_nao_encontrado(pasta)

        caminho_novo = os.path.join(pasta, novo_nome)

        if os.path.exists(caminho_novo):
            print(f"⚠️ Arquivo {novo_nome} já existe. Pulando.")
            continue

        shutil.move(caminho_original, caminho_novo)
        print(f"✅ Renomeado para: {novo_nome}")

# --------------------------------------------
# Ponto de entrada
# --------------------------------------------

def main():
    pasta = selecionar_pasta()
    if not pasta:
        print("Nenhuma pasta selecionada.")
        return

    renomear_pdfs_na_pasta(pasta)

if __name__ == "__main__":
    main()
