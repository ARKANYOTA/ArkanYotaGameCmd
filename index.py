import os
try:
    import WConio2
except:
    print("Erreur For Import WConio2")
    exit()
try:
    from varfile import * #importation of >>loc, updates, version, StyleofTyping, ARKANTitleStyle<< depuis le fichier varfile.py
except:
    print("Erreur File \"varfile\" missing")
    exit()

mapx = 1
mapy = 1
x = 64
y = 16
apparenceplayernb = 1
apparencetnb = 2
listofapparence = ["?","☺",":","_","*","%","="]
apparenceplayer = "☺"
apparencet = ":"
WConio2.setcursortype(0)
def setmapdecor():
    os.system("cls")
    global mapx, mapy
    for i in range(len(loc[mapx][mapy])): # 32 y
        for l in range(len(loc[mapx][mapy][i])): # 128 x
            if loc[mapx][mapy][i][l] == "0":
                print(" ",end="")
            elif loc[mapx][mapy][i][l] == "1":
                print("█",end="")
            else:
                print("X",end="")

os.system("mode con cols=128 lines=32")
setmapdecor()
ax = x
ay = y
while True:
    print("\033[{1};{0}H".format(x,y)+apparenceplayer,end="")
    print("\033[1;1H",end="")
    print()
    """if "os.terminal_size(columns=128, lines=32)" == str(os.get_terminal_size()):
        setmapdecor()
    else:
        os.system("mode con cols=128 lines=32")
    """    
    key = WConio2.getkey()
    aax = ax
    aay = ay
    ax = x
    ay = y
    
    if key == "up":
        if loc[mapx][mapy][y-2][x-1] == "1":
            pass
        else:
            y -= 1
    elif key == "down":
        if loc[mapx][mapy][y][x-1] == "1":
            pass
        else:
            y += 1
    elif key == "left":
        if x<2:
            aax = 128
            ax = 128
            mapx -=1
            x=128
            setmapdecor()

        else:
            if loc[mapx][mapy][y-1][x-2] == "1":
                pass
            else:
                x -= 1

    elif key == "right":
        if x>127:
            aax = 1
            ax = 1
            mapx +=1
            x=1
            setmapdecor()
        else:
            if loc[mapx][mapy][y-1][x] == "1":
                pass
            else:
                x += 1
    elif key == "\x03":
        print(exit())
    elif key == "\x1b":
        print(ARKANTitleStyle)
        EnterWhile = True
        EnterSelectOption=0
        nboptions = 4
        while EnterWhile:
            StyleofTyping(EnterSelectOption, nboptions)
            
            esckey = WConio2.getkey()
            if esckey == "\x1b": #Escap
                EnterWhile=False
            elif esckey == "\r": #Enter
                selectapparencep = True
                if EnterSelectOption%nboptions==0:
                    stykey = WConio2.getkey()
                    print("OPTIONS")
                elif EnterSelectOption%nboptions==1: #Sytle
                    
                    SelectWhile = True
                    while SelectWhile:
                        print((lambda EnterSelectOption: "\033[16;71H"+"▲ ▲" if EnterSelectOption%nboptions==1 else "\033[16;71H   ")(EnterSelectOption))
                        print((lambda EnterSelectOption: "\033[17;71H"+\
                                   (lambda selectapparencep: "\033[31m" if selectapparencep else "\033[0m")(selectapparencep)       +apparenceplayer+"\033[0m "+\
                                   (lambda selectapparencep: "\033[31m" if (not selectapparencep) else "\033[0m")(selectapparencep) +apparencet+"\033[0m" \
                               if EnterSelectOption%nboptions==1 else "\033[17;71H   ")(EnterSelectOption))
                        print((lambda EnterSelectOption: "\033[18;71H"+"▼ ▼" if EnterSelectOption%nboptions==1 else "\033[18;71H   ")(EnterSelectOption))

                        stykey = WConio2.getkey()
                        ####print(stykey)
                        if stykey == "\x16":
                            import pyperclip
                            if selectapparencep:
                                listofapparence[0] = str(pyperclip.paste())[0]
                                apparenceplayer = listofapparence[0]
                                apparenceplayernb = 0


                            else:
                                listofapparence[0] = str(pyperclip.paste())[0]
                                apparencet = listofapparence[0]
                                apparencetnb = 0
                        elif stykey == "left" or stykey == "right":
                            selectapparencep = not selectapparencep
                            print(str(selectapparencep))
                        elif stykey == "up":
                            if selectapparencep:
                                apparenceplayernb +=1
                                apparenceplayer = listofapparence[apparenceplayernb%len(listofapparence)]
                            else:
                                apparencetnb +=1
                                apparencet = listofapparence[apparencetnb%len(listofapparence)]
                        elif stykey == "down":
                            if selectapparencep:
                                apparenceplayernb-=1
                                apparenceplayer = listofapparence[apparenceplayernb%len(listofapparence)]
                            else:
                                apparencetnb -=1
                                apparencet = listofapparence[apparencetnb%len(listofapparence)]

                        elif stykey == "\x03":
                            print(exit())
                        elif stykey == "\r":
                            print("\033[16;71H   ")
                            print("\033[17;71H   ")
                            print("\033[18;71H   ")
                            SelectWhile = False
                        elif stykey == "\x1b": #Escap
                            EnterWhile=False
                            SelectWhile = False


                        
                elif EnterSelectOption%nboptions==2: #Quit
                    print(exit())
                elif EnterSelectOption%nboptions==3: #Updates
                    WConio2.clrscr()
                    print(Updates)
                    pause = WConio2.getkey()
                    if pause == "\x03":
                        print(exit())
                    EnterWhile=False
            elif esckey == "down":
                EnterSelectOption +=1
            elif esckey == "up":
                EnterSelectOption-=1

            elif esckey == "\x03":
                print(exit())
            else:
                EnterWhile=True
        setmapdecor()
    ####print("\033[1;1H",x,y)
    print("\033[{1};{0}H".format(ax,ay)+apparencet,end="")
    print("\033[{1};{0}H ".format(aax,aay),end="")


input()#Sert a rien
