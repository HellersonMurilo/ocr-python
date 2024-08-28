import fitz
from PIL import Image
import pytesseract
from io import BytesIO  # Importar BytesIO

# Abrir o arquivo PDF
documento_pdf = "alvara.pdf"
doc = fitz.open(documento_pdf)

# Loop através das páginas do PDF
for pagina_numero in range(len(doc)):
    pagina = doc.load_page(pagina_numero)
    
    # Extrair imagens da página
    imagens = pagina.get_images(full=True)
    
    # Loop através das imagens na página
    for imagem_numero, imagem_info in enumerate(imagens):
        xref = imagem_info[0]
        base_imagem = doc.extract_image(xref)
        imagem_pil = Image.open(BytesIO(base_imagem["image"]))
        
        # Utilizar OCR para extrair texto da imagem
        texto_extraido = pytesseract.image_to_string(imagem_pil)
        
        # Mostrar o texto extraído
        print(f"Texto extraído da imagem {imagem_numero + 1} na página {pagina_numero + 1}:\n{texto_extraido}")
