import os
import re
import pytesseract
import fitz  # PyMuPDF
from pdf2image import convert_from_path
from PIL import Image
from tkinter import filedialog, Tk
import shutil

# Caminho para o executável do Tesseract OCR (ajuste se necessário)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def selecionar_pasta():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Selecione a pasta com os PDFs")

def extrair_numero_nota(texto):
    # Ajuste esta expressão conforme o padrão exato dos seus documentos
    match = re.search(r'(?:NF(?:-e)?|Nota Fiscal|Nº)[^\d]{0,10}(\d{4,})', texto, re.IGNORECASE)
    return match.group(1) if match else None

def extrair_texto(pdf_path):
    texto_extraido = ""

    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            texto_extraido += page.get_text()
        doc.close()

        if texto_extraido.strip():
            return texto_extraido
    except:
        pass

    # Se não conseguiu extrair texto, tenta OCR
    try:
        imagens = convert_from_path(pdf_path, dpi=300)
        for img in imagens:
            texto_extraido += pytesseract.image_to_string(img, lang='por')
    except Exception as e:
        print(f"OCR falhou para {pdf_path}: {e}")

    return texto_extraido


def renomear_pdfs_na_pasta(pasta):
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")]

    for arquivo in arquivos:
        caminho_original = os.path.join(pasta, arquivo)
        print(f"Processando: {arquivo}")

        texto = extrair_texto(caminho_original)

        print(f"Texto extraído do arquivo {arquivo}:\n")
        print(texto)  # imprime o texto para análise
        print("----")

        numero_nota = extrair_numero_nota(texto)

        if numero_nota:
            novo_nome = f"{numero_nota}.pdf"
            caminho_novo = os.path.join(pasta, novo_nome)

            if os.path.exists(caminho_novo):
                print(f"Arquivo com número {numero_nota} já existe. Pulando.")
                continue

            shutil.move(caminho_original, caminho_novo)
            print(f"Renomeado para: {novo_nome}")
        else:
            print(f"⚠️ Número da nota não encontrado em: {arquivo}")
    

def main():
    pasta = selecionar_pasta()
    if not pasta:
        print("Nenhuma pasta selecionada.")
        return

    renomear_pdfs_na_pasta(pasta)

if __name__ == "__main__":
    main()
