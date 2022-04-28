from PIL import Image

colorImage = Image.open("./9god.jpeg") # Poner la imagen

rotated = colorImage.rotate(180)
rotated.show()
rotated.save("thereal9dog.jpeg", "JPEG")
