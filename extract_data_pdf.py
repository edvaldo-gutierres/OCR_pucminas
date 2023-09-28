# Importa biblioteca
import fitz

# Função para extrair texto de um arquivo PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_document = fitz.open(pdf_file)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            page_text = page.get_text()
            text += page_text
    except Exception as e:
        text = f"Error: {str(e)}"
    return text

# Nome do arquivo PDF que você deseja processar
pdf_file = "assets/doc/previa.pdf"  # Substitua pelo caminho do seu arquivo PDF

# Chama a função para extrair texto do PDF
extracted_text = extract_text_from_pdf(pdf_file)

# Imprime o texto extraído
print(extracted_text)
