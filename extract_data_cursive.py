from pdf2image import convert_from_path
import pytesseract

# Informa o caminho do Poppler
poppler_path = r'assets\poppler-23.08.0\Library\bin'

# Caminho do executável do pytesseract
pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\Tesseract.exe"

# Informa o caminho do modelo treinado para o idioma português
config = '--tessdata-dir assets/tessdata'
# config = r'--oem 3 --psm 6'


# Função para extrair texto de uma imagem usando OCR
def extract_text_from_image(image):
    return pytesseract.image_to_string(image, lang='por', config=config)


# Nome do arquivo PDF que você deseja processar
pdf_file = "assets/doc/doc1.pdf"  # Substitua pelo caminho do seu arquivo PDF
pdf_text = ""

try:
    # Converte as páginas PDF em imagens
    pages = convert_from_path(pdf_file, poppler_path=poppler_path)

    for page_num, image in enumerate(pages):
        # Aplica OCR para extrair texto da imagem
        image_text = extract_text_from_image(image)

        # Adiciona o texto extraído ao texto do PDF
        pdf_text += f"Page {page_num + 1}:\n{image_text}\n\n"
except Exception as e:
    pdf_text = f"Error: {str(e)}"

# Imprime o texto extraído
print(pdf_text)
