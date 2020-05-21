import os, WConio2
from varfile import * #importation of >>loc, updates, version, StyleofTyping, ARKANTitleStyle<< depuis le fichier varfile.py
from WConio2 import getkey, setcursortype

def setmapdecor():
    print("\033[1;1H\033[2J")#os.system("cls")
    global mapx, mapy
    for i in range(len(loc[mapx][mapy])): # 32 y
        for l in range(len(loc[mapx][mapy][i])): # 128 x
            a = loc[mapx][mapy][i][l]
            #print((lambda: " " if a=="0" else("█" if a=="1" else "X"))(),end="")
            print((lambda: " " if a=="0" else "")(),end="")
            print((lambda: "█" if a=="1"else "")(),end="")
            print((lambda: "X" if (a!="0" and a!="1") else "")(),end="")

CtrlC = lambda key: exit() if key == "\x03" else None

os.system("mode con cols=128 lines=32")
setcursortype(0)
setmapdecor()

while True:
    print("\033[{1};{0}H".format(x,y)+apparenceplayer,end="")
    print("\033[1;1H",end="")
    print()

    key = getkey()
    if key == "down" or key == "up" or key == "right" or key == "left":
        aax, aay, ax , ay = ax, ay, x, y
    
    if key == "up":
        if y<2:
            aay, ay, y = 30, 30, 30
            mapy -=1
            setmapdecor()
            
        if loc[mapx][mapy][y-2][x-1] == "1":
            pass
        else:
            y -= 1
    elif key == "down":
        if y>30:
            aay, ay, y = 2, 2, 2
            mapy +=1
            setmapdecor()

        if loc[mapx][mapy][y][x-1] == "1":
            pass
        else:
            y += 1
    elif key == "left":
        if x<2:
            aax, ax, x = 128, 128, 128
            mapx -=1
            setmapdecor()

        else:
            if loc[mapx][mapy][y-1][x-2] == "1":
                pass
            else:
                x -= 1

    elif key == "right":
        if x>127:
            aax, ax, x = 1, 1, 1
            mapx +=1
            setmapdecor()
        else:
            if loc[mapx][mapy][y-1][x] == "1":
                pass
            else:
                x += 1
    #elif key == "\x03":
     #   exit()
    elif key == "\x1b":
        print(ARKANTitleStyle)
        EnterWhile = True
        EnterSelectOption, nboptions = 0, 4
        while EnterWhile:
            StyleofTyping(EnterSelectOption, nboptions)
            
            esckey = getkey()
            CtrlC(esckey)
            if esckey == "\x1b": #Escap
                EnterWhile=False
            elif esckey == "\r": #Enter
                selectapparencep = True
                if EnterSelectOption%nboptions==0: #Options
                    AffichefenetreOptions()
                    OptionWhile = True
                    while OptionWhile:
                        optkey = getkey()
                        CtrlC(optkey)
                        if optkey=="\x1b": #Escap
                            OptionWhile = False
                            EnterWhile = False
                        
                        
                elif EnterSelectOption%nboptions==1: #SAVE
                    pass
                elif EnterSelectOption%nboptions==2: #MENU
                    pass
                elif EnterSelectOption%nboptions==3: #QUIT
                    exit()
            elif esckey == "down":
                EnterSelectOption +=1
            elif esckey == "up":
                EnterSelectOption-=1

            
            else:
                EnterWhile=True
        setmapdecor()
    CtrlC(key)
    ####print("\033[1;1H",x,y)
    print("\033[{1};{0}H".format(ax,ay)+apparencet,end="")
    print("\033[{1};{0}H ".format(aax,aay),end="")


input()#Sert a rien

