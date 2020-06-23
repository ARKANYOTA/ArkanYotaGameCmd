from PIL import Image
jk, rk = 0,0
x, y = 128, 3
for jr in range(3):
    for rr in range(3):
        img = Image.open("loc["+str(jr)+"]["+str(rr)+"].jpg")
        lar, hau = img.size
        newimg = Image.new("RGB", (lar, hau))
        for l in range(hau):
            for c in range(lar):
                pix = img.getpixel((c, l))
                gris = int((pix[0]+pix[1]+pix[2])/100)
                r,g,b = gris,gris,gris
                newimg.putpixel((c, l),(r, g, b))

        data = list(newimg.getdata())
        final = "loc["+str(jr)+"]["+str(rr)+"] = [\""
        k = 0
        for i in data:
            k+=1
            final += str(i).replace("(2, 2, 2)", "a").replace("(3, 3, 3)", "a").replace("(6, 6, 6)", "0").replace("(7, 7, 7)", "0").replace("(0, 0, 0)", "1").replace("(1, 1, 1)", "a")
            if k%128==0:
                if k<4000:
                    final+="\",\\\n             \""
                else:
                    final+="\"]"
        print()
        print(final)
input()

"""
from PIL import Image

img = Image.open("loc[0][0].jpg")
x, y = 128, 3
lar, hau = img.size
newimg = Image.new("RGB", (lar, hau))

for l in range(hau):
    for c in range(lar):
        pix = img.getpixel((c, l))
        gris = int((pix[0]+pix[1]+pix[2])/100)

        r,g,b = gris,gris,gris
        newimg.putpixel((c, l),(r, g, b))

#newimg.show()
data = list(newimg.getdata())
j = 0
final = ""
k = 0
for i in data:

    k+=1
    final += str(i).replace("(2, 2, 2)", "X").replace("(6, 6, 6)", " ").replace("(7, 7, 7)", " ").replace("(0, 0, 0)", "V").replace("(1, 1, 1)", "X")
    if k%128==0:
        final+="\n"
    #j+=1

            
print(l,"/", c,"/", lar,"//",hau)
print()
print("---------------------------------------------------")
v = 0

print(final)
#print(data)

input()

"""















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
