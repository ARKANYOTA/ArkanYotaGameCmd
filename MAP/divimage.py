from PIL import Image

ima = Image.open("MAP.png")
x, y = ima.size
l = 192
# a vous de trouver l
for i in range(3):
    for y in range(3):
        im = Image.new("RGB", (128, 32), "white")
        im.paste(ima, (-128*i, -32*y))
        im.save("loc[{0}][{1}].jpg".format(i, y), "JPEG")


    
"""
im1 = Image.new("RGB", (l, y), "white") # Partie gauche
im1.paste(im, (0, 0, x, y))
im1.save("test1.jpg", "JPEG")
"""
