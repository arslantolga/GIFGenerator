from PIL import Image
import os

yol = "PNG"
yollar = []
images = []

for i in os.listdir(yol):
    yollar.append(yol+'/'+i)

for path in yollar:
     image = Image.open(path)
     images.append(image)

images[0].save('animasyon.gif', format='GIF', append_images=images[1:], save_all=True, duration=300, loop=0)