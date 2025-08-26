import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader, PdfWriter

def selecionar_pasta():
    root = Tk()
    root.withdraw()  # Oculta a janela principal
    pasta = filedialog.askdirectory(title="Selecione a pasta com o PDF")
    return pasta

def dividir_pdf_em_paginas(caminho_pdf, pasta_destino):
    nome_arquivo_base = os.path.splitext(os.path.basename(caminho_pdf))[0]
    pdf = PdfReader(caminho_pdf)

    for i, pagina in enumerate(pdf.pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pagina)

        nome_saida = f"{nome_arquivo_base}_pagina_{i+1}.pdf"
        caminho_saida = os.path.join(pasta_destino, nome_saida)

        with open(caminho_saida, "wb") as f:
            pdf_writer.write(f)

        print(f"Página {i+1} salva como {nome_saida}")

def main():
    pasta = selecionar_pasta()

    if not pasta:
        print("Nenhuma pasta selecionada.")
        return

    # Procura pelo primeiro arquivo .pdf na pasta
    pdfs = [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")]

    if not pdfs:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return

    caminho_pdf = os.path.join(pasta, pdfs[0])
    print(f"Dividindo o arquivo: {caminho_pdf}")
    dividir_pdf_em_paginas(caminho_pdf, pasta)

if __name__ == "__main__":
    main()
