import os
import requests

urlBase = "https://www.conaliteg.sep.gob.mx/2023/c/"

#Al usar esta url un tanto diferente podemos acceder directmente a donde se encuentre guardada la imágen, por lo tanto si no existe, no bajará ningún archivo 

links = [
    "P1MLA",
    "P1PAA",
    "P1PCA",
    "P1TPA",
    "P1SDA",
    "P1PEA",
    # Agrega más enlaces aquí
]



# Rango de imágenes a descargar (por ejemplo, del 1 al 100)
#inicioIndex = 1
#finalIndex = 300

#Ya no es necesario usar un rango de imagenes

# Carpeta de destino para guardar las imágenes descargadas
folderDestino = os.path.join(os.getcwd(), "librosPrimerGrado")
os.mkdir(folderDestino)

#De esta manera podemos crear la carpeta sin necesidad de tener permisos extras

for link in links:

    count = 0
    seguir = True

    full_url = urlBase + link

    while seguir:
        imagenUrl = f"{full_url}/{count:03d}.jpg"

        response = requests.get(imagenUrl)
        if response.status_code == 200:
            imagenNombreSecuencia = f"{link}_{count:03d}.jpg"
            imagenPath = os.path.join(folderDestino, imagenNombreSecuencia)

            with open(imagenPath, "wb") as img_file:
                img_file.write(response.content)

            print(f"Imagen {imagenNombreSecuencia} descargada")
            count += 1

        else:
            print(f"Error al descargar la imagen {imagenUrl}")
            seguir = False

print("Proceso de descarga de imágenes completado.")
