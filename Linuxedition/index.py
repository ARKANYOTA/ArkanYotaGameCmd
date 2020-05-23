# -*- coding: utf-8 -*-
import os
from ubuntuvarfile import * #importation of >>loc, updates, version, StyleofTyping, ARKANTitleStyle<< depuis le fichier varfile.py
#from WConio2 import getk
from chtest import getkey

def cls():
    print("\033[1;1H\033[2J")
def setmapdecor():
    cls() #print("\033[1;1H\033[2J")#os.system("cls")
    global mapx, mapy
    for i in range(len(loc[mapx][mapy])): # 32 y
        print()
        print("\033[2K\033[{0};1H".format(i+1), end='')
        for l in range(len(loc[mapx][mapy][i])): # 128 x
            a = loc[mapx][mapy][i][l]
            #print((lambda: " " if a=="0" else("█" if a=="1" else "X"))(),end="")
            print((lambda: " " if a=="0" else "")(),end="")
            print((lambda: "█" if a=="1"else "")(),end="")
            print((lambda: "\033[32m█\033[0m" if a=="a"else "")(),end="")
            print((lambda: "X" if (a not in "01a") else "")(),end="")

os.system("mode con cols=128 lines=32")
print("\033[?25l") #setcursortype(0)
#print("\033[?25h") #setcursortype(1)
setmapdecor()

while True:
    print("\033[{1};{0}H".format(x,y)+apparenceplayer,end="")
    print("\033[1;1H",end="")
    print()

    key = getkey()
    #if key == "down" or key == "up" or key == "right" or key == "left":
     #   aax, aay, ax , ay = ax, ay, x, y
    
    if key == "up":
        if y<2:
            aay, ay, y = 33, 33, 33
            mapy -=1
            setmapdecor()
            
        if loc[mapx][mapy][y-2][x-1] in fullblock:
            pass
        else:
            aax, aay, ax , ay, direction = ax, ay, x, y, "up"
            y -= 1
    elif key == "down":
        if y>31:
            aay, ay, y = 0, 0, 0
            mapy +=1
            setmapdecor()

        if loc[mapx][mapy][y][x-1] in fullblock:
            pass
        else:
            aax, aay, ax , ay, direction = ax, ay, x, y, "down"
            y += 1
    elif key == "left":
        if x<2:
            aax, ax, x = 128, 128, 128
            mapx -=1
            setmapdecor()

        else:
            if loc[mapx][mapy][y-1][x-2] in fullblock:
                pass
            else:
                aax, aay, ax , ay, direction = ax, ay, x, y, "left"
                x -= 1

    elif key == "right":
        if x>127:
            aax, ax, x = 1, 1, 1
            mapx +=1
            setmapdecor()
        else:
            if loc[mapx][mapy][y-1][x] in fullblock:
                pass
            else:
                aax, aay, ax , ay, direction= ax, ay, x, y, "right"
                x += 1
    elif key == b"\n":
        if (loc[mapx][mapy][y-1][x] in InteractBlock and direction=="right")or \
           (loc[mapx][mapy][y-1][x-2] in InteractBlock and direction=="left") or\
           (loc[mapx][mapy][y-2][x-1] in InteractBlock and direction=="up") or\
           (loc[mapx][mapy][y][x-1] in InteractBlock and direction=="down"):
            print("\033[11;11Hsi")
        print("\033[10;10H"+direction)
    elif key == b"g":
        print(ARKANTitleStyle)
        EnterWhile = True
        EnterSelectOption, nboptions = 0, 4
        while EnterWhile:
            StyleofTyping(EnterSelectOption, nboptions)
            OptionSelectOption, nbptionoptions = 0, 11
            esckey = getkey()
            if esckey == b"g": #Escap
                EnterWhile=False
            elif esckey == "down":
                EnterSelectOption +=1
            elif esckey == "up":
                EnterSelectOption-=1
            elif esckey == b"\n": #Enter
                selectapparencep = True
                if EnterSelectOption%nboptions==0: #Options
                    AffichefenetreOptions()
                    OptionWhile = True
                    while OptionWhile:
                        OptionofTyping(OptionSelectOption, nbptionoptions)
                        optkey = getkey()
                        if optkey==b"g": #Escap
                            OptionWhile = False
                            EnterWhile = False
                        if optkey==b"\n": #Escap
                            setmapdecor()
                            print(ARKANTitleStyle)
                            OptionWhile = False
                        elif optkey == "down":
                            OptionSelectOption +=1
                        elif optkey == "up":
                            OptionSelectOption-=1
                            
                elif EnterSelectOption%nboptions==1: #SAVE
                    pass
                elif EnterSelectOption%nboptions==2: #MENU
                    pass
                elif EnterSelectOption%nboptions==3: #QUIT
                    exit()

        setmapdecor()
    
    print("\033[{1};{0}H".format(ax,ay)+apparencet,end="")
    print("\033[{1};{0}H ".format(aax,aay),end="")
    


