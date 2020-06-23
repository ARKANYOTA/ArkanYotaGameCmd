from sys import platform
from os import system
from time import sleep
from Var import *
from Loc import *
from Get import getkey

#Mettre l'invite de commande à vide
system("mode con cols=128 lines=32")
print("\033[?25l")

def setmapdecor():
    VarSetMapDecor(mapx, mapy, loc)

def message(msg):
    VarMessage(msg, x, y)
    setmapdecor()

def inventory():
    VarInventory(x,y)
    setmapdecor()


  
while True:
    print("\033[1;1H\033[2J", end="")
    PrintEcrandacceuil()
    menukey = getkey()
    CtrlC(menukey)
    GAME = True
    setmapdecor()
    while GAME:
        print("\033[{1};{0}H".format(x,y)+apparenceplayer,end="")
        print("\033[1;1H",end="")
        if F3Mode:
            if OldCoteeIsGauche != IsCoteeGauche:
                setmapdecor()
            OldCoteeIsGauche = IsCoteeGauche
            if x < 64: IsCoteeGauche = True
            else: IsCoteeGauche = False
            if IsCoteeGauche:
                print("\033[4;90HX:", x, "Y:", y, "     ")
                print("\033[5;90HMapX:", mapx, "MapY:", mapy, "     ")
                print("\033[6;90HDIR:", direction, "  ", "     ")
                print("\033[7;90H"+version, "     ")
                print("\033[8;90H" + sysexp, "     ")
            else:
                print("\033[4;4HX:", x, "Y:", y, "     ")
                print("\033[5;4HMapX:", mapx, "MapY:", mapy, "     ")
                print("\033[6;4HDIR:", direction, "  ", "     ")
                print("\033[7;4H"+version, "     ")
                print("\033[8;4H"+sysexp, "     ")
        print()
        key = getkey()
        CtrlC(key)
        if key == openmsg:
            message("$print('Yo')¶HELLOµBonjoiurJeµPooooooooµa¶Its not trueµbeacause¶Its false")
        elif key == invsee:
            inventory()
        elif key == up:
            if y<2: aay, ay, y = 32, 32, 32; mapy -=1; setmapdecor()
            else:
                if loc[mapx][mapy][y-2][x-1] in fullblock:
                    pass
                else:
                    aax, aay, ax , ay = ax, ay, x, y; y -= 1
            direction = "up"
            
        elif key == down:
            if y>31: aay, ay, y = 1, 1, 1; mapy +=1; setmapdecor()
            else:
                if loc[mapx][mapy][y][x-1] in fullblock:
                    pass
                else:
                    aax, aay, ax , ay = ax, ay, x, y; y += 1
            direction = "down"
            
        elif key == left:
            if x<2: aax, ax, x = 128, 128, 128; mapx -=1; setmapdecor()
            else:
                if loc[mapx][mapy][y-1][x-2] in fullblock:
                    pass
                else:
                    aax, aay, ax , ay = ax, ay, x, y; x -= 1
            direction = "left"

        elif key == right:
            if x>127: aax, ax, x = 1, 1, 1; mapx +=1; setmapdecor()
            else:
                if loc[mapx][mapy][y-1][x] in fullblock:
                    pass
                else:
                    aax, aay, ax , ay = ax, ay, x, y; x += 1
            direction = "right"

        elif key == enter:
            if (loc[mapx][mapy][y-1][x] in InteractBlock and direction=="right"):
                if str(loc[mapx][mapy][y-1][x]) in dicomsg:
                    message(dicomsg[str(loc[mapx][mapy][y-1][x])])
            elif (loc[mapx][mapy][y-1][x-2] in InteractBlock and direction=="left"):
                if str(loc[mapx][mapy][y-1][x-2]) in dicomsg:
                    message(dicomsg[str(loc[mapx][mapy][y-1][x-2])])
            elif (loc[mapx][mapy][y-2][x-1] in InteractBlock and direction=="up"):
                if str(loc[mapx][mapy][y-2][x-1]) in dicomsg:
                    message(dicomsg[str(loc[mapx][mapy][y-2][x-1])])
            elif (loc[mapx][mapy][y][x-1] in InteractBlock and direction=="down"):
                if str(loc[mapx][mapy][y][x-1]) in dicomsg:
                    message(dicomsg[str(loc[mapx][mapy][y][x-1])])
                
        elif key == f3:
            F3Mode = not F3Mode
            setmapdecor()
        elif key == invsee:
            InvWhile = True
            while InvWhile:
                print("\033[10;10H",money)
                invkey = getkey()
                CtrlC(invkey)
                
                if invkey == escap:
                    InvWhile = False
                    setmapdecor()
                elif invkey == down: pass
                elif invkey == up: pass
        elif key == escap:
            print(ARKANTitleStyle)
            EnterWhile = True
            EnterSelectOption, nboptions = 0, 4
            while EnterWhile:
                StyleofTyping(EnterSelectOption, nboptions)
                OptionSelectOption, nbptionoptions = 0, 11
                esckey = getkey()
                CtrlC(esckey)
                if esckey == escap:
                    EnterWhile=False
                
                elif esckey == down:
                    EnterSelectOption +=1
                
                elif esckey == up:
                    EnterSelectOption-=1
                
                elif esckey == enter: 
                    selectapparencep = True
                    if EnterSelectOption%nboptions==0: #Options
                        AffichefenetreOptions()
                        OptionWhile = True
                        while OptionWhile:
                            OptionofTyping(OptionSelectOption, nbptionoptions)
                            optkey = getkey()
                            CtrlC(optkey)
                            if optkey==escap:
                                OptionWhile = False;
                                EnterWhile = False
                            
                            elif optkey == down:
                                OptionSelectOption +=1
                            
                            elif optkey == up:
                                OptionSelectOption-=1
                            
                            elif optkey==delete: 
                                setmapdecor()
                                print(ARKANTitleStyle)
                                OptionWhile = False

                            elif optkey==enter:
                                if OptionSelectOption%nbptionoptions==0:
                                    setmapdecor()
                                    AffichefenetreOptionsContols()
                                    ControlsWhile=True
                                    controlnombre = 0
                                    while ControlsWhile:
                                        nbopt = 10
                                        v = controlnombre%nbopt
                                        print((lambda: "\033[8;7H \033[31m up  \033[0m" if v==0 else "\033[8;7H up   ")() + str(up.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[9;7H \033[31m down  \033[0m" if v==1 else "\033[9;7H down   ")() + str(down.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[10;7H \033[31m right  \033[0m" if v==2 else "\033[10;7H right   ")() + str(right.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[11;7H \033[31m left  \033[0m" if v==3 else "\033[11;7H left    ")() + str(left.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[12;7H \033[31m escap  \033[0m" if v==4 else "\033[12;7H escap    ")() + str(escap.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[13;7H \033[31m enter  \033[0m" if v==5 else "\033[13;7H enter   ")() + str(enter.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[14;7H \033[31m delete  \033[0m" if v==6 else "\033[14;7H delete    ")() + str(delete.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[15;7H \033[31m f3  \033[0m" if v==7 else "\033[15;7H f3    ")() + str(f3.encode("UTF-8")) + " "*30)
                                        print((lambda: "\033[16;7H \033[31m RESET  \033[0m" if v==8 else "\033[16;7H RESET    ")())
                                        print((lambda: "\033[17;7H \033[31m SAVE  \033[0m" if v==9 else "\033[17;7H SAVE    ")())

                                        ctrlkey = getkey()
                                        CtrlC(ctrlkey)
                                        if ctrlkey==escap: 
                                            ControlsWhile = False
                                            OptionWhile = False
                                            EnterWhile = False
                                        elif ctrlkey==delete: 
                                            setmapdecor()
                                            AffichefenetreOptions()
                                            ControlsWhile = False
                                        elif ctrlkey==enter:
                                            if controlnombre%nbopt==0:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                up = controlgetkey
                                            elif controlnombre%nbopt==1:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                down = controlgetkey
                                            elif controlnombre%nbopt==2:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                right = controlgetkey
                                            elif controlnombre%nbopt==3:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                left= controlgetkey
                                            elif controlnombre%nbopt==4:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                escap = controlgetkey
                                            elif controlnombre%nbopt==5:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                enter = controlgetkey
                                            elif controlnombre%nbopt==6:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                delete = controlgetkey
                                            elif controlnombre%nbopt==7:
                                                controlgetkey = getkey()
                                                CtrlC(controlgetkey)
                                                f3 = controlgetkey
                                            elif controlnombre%nbopt==8:
                                                if platform[:3] == 'win':
                                                    up = 'up'
                                                    down = 'down'
                                                    right = 'right'
                                                    left = 'left'
                                                    escap = '\x1b'
                                                    enter = '\r'
                                                    delete = '\x08'
                                                    f3 = 'f3'
                                                elif platform[:3] == 'lin' or platform[:3] == 'dar':
                                                    up = '\x1b[A'
                                                    down = '\x1b[B'
                                                    right = '\x1b[C'
                                                    left= '\x1b[D'
                                                    escap = '\x1b\x1b'
                                                    enter = '\r'
                                                    delete = '\x7f'
                                                    f3 = '\x1bO'
                                            elif controlnombre%nbopt==9:
                                                if platform[:3] == 'win':
                                                    keysave = "winkeysave.txt"
                                                elif platform[:3] == 'lin' or platform[:3] == 'dar':
                                                    keysave = "linkeysave.txt"
                                                with open(keysave, mode='w') as f:
                                                    f.write(str((up))+"¶")
                                                    f.write(str((down))+"¶")
                                                    f.write(str((right))+"¶")
                                                    f.write(str((left))+"¶")
                                                    f.write(str((escap))+"¶")
                                                    f.write(str((enter))+"¶")
                                                    f.write(str((delete))+"¶")
                                                    f.write(str((f3)))              
                                        elif ctrlkey==up:
                                            controlnombre -=1
                                        elif ctrlkey==down:
                                            controlnombre +=1

                    elif EnterSelectOption%nboptions==1: #SAVE
                        pass
                    elif EnterSelectOption%nboptions==2: #MENU
                        GAME = False
                        break
                    elif EnterSelectOption%nboptions==3: #QUIT
                        exit()

            setmapdecor()
        
        print("\033[{1};{0}H".format(ax,ay)+apparencet,end="")
        print("\033[{1};{0}H ".format(aax,aay),end="")
