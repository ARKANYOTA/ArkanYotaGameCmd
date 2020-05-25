from PIL import Image

img = Image.open("loc[0][0].jpg")
x, y = 128, 3
lar, hau = img.size
newimg = Image.new("RGB", (lar, hau))

for l in range(hau):
    for c in range(lar):
        pix = img.getpixel((c, l))
        gris = int((pix[0]+pix[1]+pix[2])/3)

        r,g,b = gris,gris,gris
        newimg.putpixel((c, l),(r, g, b))

#newimg.show()
data = list(newimg.getdata())
j = 0
final = ""
for i in data:
    final += str(i).replace("(255, 255, 255)", "X").replace("(69, 69, 69)", "O").replace("(0, 0, 0)", "V")
    #j+=1

            
print(l,"/", c,"/", lar,"//",hau)
print()
print("---------------------------------------------------")
v = 0

print(final)
input()
"""
else:
            print(i, "/", j, "/hau :", j%x, "/long : ", int(j/384))
            final[-1] += " "

    if j%x == 0:
        final.append("")
    if i == (0,0,0) or i == (1,1,1):
        final[-1] += "\033[31m█\033[0m"
    elif i == (134, 134, 134):
        final[-1] += "\033[32m█\033[0m"
    elif i == (69, 69, 69) or i == (70, 70, 70) or i == (71, 71, 71) or i == (72, 72, 72):
        final[-1] += "\033[34m█\033[0m"
    elif i == (254,254,254) or i == (255,255,255):
        final[-1] += "\033[33m█\033[0m"
    else:
        print(i, "/", j, "/hau :", j%x, "/long : ", int(j/384))
        final[-1] += " "
    """ 
