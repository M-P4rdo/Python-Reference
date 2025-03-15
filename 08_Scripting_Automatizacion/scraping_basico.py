#---------- Web Scraping ----------
import requests
import bs4

#(Extraer Título):
url = "https://example.com"
respuesta = requests.get(url)

soup = bs4.BeautifulSoup(respuesta.text, "html.parser")
titulo = soup.title.text
print(f"Título de la página: {titulo}")

#(Extraer Enlaces):
enlaces = soup.find_all("a")
for enlace in enlaces:
    print(enlace.get("href"))

#(Descargar imágenes):
import os

imagenes = soup.find_all("img")
for img in imagenes:
    src = img.get("src")
    if src.startswith("http"):
        img_data = requests.get(src).content
        nombre = os.path.basename(src)
        
        with open(nombre, "wb") as file:
            file.write(img_data)

print("Imágenes descargadas")