import os
import requests
from urllib.parse import urlparse
from PyPDF2 import PdfReader

def descargar_pdf(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as f:
        f.write(response.content)

def buscar_texto_en_pdf(archivo_pdf, texto_busqueda):
    texto_encontrado = False
    with open(archivo_pdf, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            if texto_busqueda in page.extract_text():
                texto_encontrado = True
                break
    return texto_encontrado

def main():
    texto_busqueda = input("Enter text string to be searched: ")
    nombre_archivo = input("Enter text filename having PDF URLs where I'm going to search (e.g. list.txt): ")

    with open(nombre_archivo, 'r') as file:
        for line in file:
            url = line.strip()
            nombre_archivo_pdf = os.path.basename(urlparse(url).path)
            descargar_pdf(url, nombre_archivo_pdf)
            if buscar_texto_en_pdf(nombre_archivo_pdf, texto_busqueda):
                print("Texto encontrado en:", url)
            else:
                print("Texto no encontrado en:", url)
            os.remove(nombre_archivo_pdf)

if __name__ == "__main__":
    main()
