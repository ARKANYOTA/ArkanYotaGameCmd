from sys import platform
from Get import getkey

version = "Beta Multi-Edition 1.1.2"
#A sauvgarder dans le fichier saves.txt
direction = "up"
lang = "fr"
money = 1000
mapx, mapy= 1, 1
x, y = 64 , 16
ax, ay = 64 , 15
aax, aay = 64, 14
level = 0

"""
apparenceplayernb = 1
apparencetnb = 2
listofapparence = ["?","☺",":","_","*","%","="]
"""
apparenceplayer = "☺"
apparencet = ":"

fullblock = "b1!*"
InteractBlock = "!*"
dicomsg = {"!": "Hello", "*": "Deuxieme message"}
GAME = True
F3Mode = False
IsCoteeGauche = True
OldCoteeIsGauche = True

msglist = ["Message n°1", "Message n°2"]

#Valeur à mettre dans win(lin)keysave.txt
openmsg = "l"
invsee = "e"


def CtrlC(key):
    if key == '\x03':
        exit()    
    else:
        None

if platform[:3] == 'win':
    sysexp = "Win"
    try:
        with open('winkeysave.txt', 'rb') as f:
            allkeylist = f.readline()
        allkeylistafter = allkeylist.split(b'\xb6')
        up = allkeylistafter[0].decode()
        down = allkeylistafter[1].decode()
        right = allkeylistafter[2].decode()
        left= allkeylistafter[3].decode()
        escap = allkeylistafter[4].decode()
        enter = allkeylistafter[5].decode()
        delete = allkeylistafter[6].decode()
        f3 = allkeylistafter[7].decode()
    except:
        up = 'up'
        down = 'down'
        right = 'right'
        left= 'left'
        escap = '\x1b'
        enter = '\r'
        delete = '\x08'
        f3 = 'f3'
        
elif platform[:3] == 'lin' or platform[:3] == 'dar':
    if platform[:3] == 'lin': sysexp = "Lin"
    else: sysexp = "Mac"
    try:
        with open('linkeysave.txt', 'rb') as f:
            allkeylist = f.readline()
        allkeylistafter = allkeylist.split(b'\xb6')
        up = allkeylistafter[0].decode()
        down = allkeylistafter[1].decode()
        right = allkeylistafter[2].decode()
        left= allkeylistafter[3].decode()
        escap = allkeylistafter[4].decode()
        enter = allkeylistafter[5].decode()
        delete = allkeylistafter[6].decode()
        f3 = allkeylistafter[7].decode()
    except:
        up = '\x1b[A'
        down = '\x1b[B'
        right = '\x1b[C'
        left= '\x1b[D'
        escap = '\x1b\x1b'
        enter = '\r'
        delete = '\x7f'
        f3 = '\x1bO'

def cls():
    print("\033[1;1H\033[2J")

def StyleofTyping(EnterSelectOption, nboptions):
    a = EnterSelectOption%nboptions
    print((lambda: "\033[13;50H \033[31m ╔═╗╔═╗╔╦╗╦╔═╗╔╗╦╔═╗  \033[0m" if a==0 else "\033[13;50H ╔═╗╔═╗╔╦╗╦╔═╗╔╗╦╔═╗   ")())
    print((lambda: "\033[14;50H \033[31m ║ ║╠═╝ ║ ║║ ║║║║╚═╗  \033[0m" if a==0 else "\033[14;50H ║ ║╠═╝ ║ ║║ ║║║║╚═╗   ")())
    print((lambda: "\033[15;50H \033[31m ╚═╝╩   ╩ ╩╚═╝╩╚╝╚═╝  \033[0m" if a==0 else "\033[15;50H ╚═╝╩   ╩ ╩╚═╝╩╚╝╚═╝   ")())
    print((lambda: "\033[16;50H \033[31m ╔═╗╔═╗╦ ╦╔═╗╔═╗  \033[0m" if a==1 else "\033[16;50H ╔═╗╔═╗╦ ╦╔═╗╔═╗    ")())
    print((lambda: "\033[17;50H \033[31m ╚═╗╠═╣║ ║╠╣ ╚═╗  \033[0m" if a==1 else "\033[17;50H ╚═╗╠═╣║ ║╠╣ ╚═╗    ")())
    print((lambda: "\033[18;50H \033[31m ╚═╝╩ ╩╚╦╝╚═╝╚═╝  \033[0m" if a==1 else "\033[18;50H ╚═╝╩ ╩╚╦╝╚═╝╚═╝    ")())
    print((lambda: "\033[19;50H \033[31m ╔╦╗╔═╗╔╗╦╦ ╦  \033[0m" if a==2 else "\033[19;50H ╔╦╗╔═╗╔╗╦╦ ╦    ")())
    print((lambda: "\033[20;50H \033[31m ║╩║╠╣ ║║║║ ║  \033[0m" if a==2 else "\033[20;50H ║╩║╠╣ ║║║║ ║    ")())
    print((lambda: "\033[21;50H \033[31m ╩ ╩╚═╝╩╚╝╚═╝  \033[0m" if a==2 else "\033[21;50H ╩ ╩╚═╝╩╚╝╚═╝    ")())
    print((lambda: "\033[22;50H \033[31m ╔═╗╦ ╦╦╔╦╗  \033[0m" if a==3 else "\033[22;50H ╔═╗╦ ╦╦╔╦╗    ")())
    print((lambda: "\033[23;50H \033[31m ║╦║║ ║║ ║   \033[0m" if a==3 else "\033[23;50H ║╦║║ ║║ ║     ")())
    print((lambda: "\033[24;50H \033[31m ╚╬╝╚═╝╩ ╩   \033[0m" if a==3 else "\033[24;50H ╚╬╝╚═╝╩ ╩     ")())

def OptionofTyping(OptionSelectOption, nbptionoptions):
    a = OptionSelectOption%nbptionoptions
    print((lambda: "\033[8;7H \033[31m Controls  \033[0m" if a==0 else "\033[8;7H Controls   ")())
    print((lambda: "\033[9;7H \033[31m music  \033[0m" if a==1 else "\033[9;7H music   ")())
    print((lambda: "\033[10;7H \033[31m lang  \033[0m" if a==2 else "\033[10;7H lang   ")())
    print((lambda: "\033[11;7H \033[31m Settings  \033[0m" if a==3 else "\033[11;7H Settings    ")())
    print((lambda: "\033[12;7H \033[31m Visuel  \033[0m" if a==4 else "\033[12;7H Visuel    ")())
    print((lambda: "\033[13;7H \033[31m Textures  \033[0m" if a==5 else "\033[13;7H Textures   ")())
    print((lambda: "\033[14;7H \033[31m Comptes  \033[0m" if a==6 else "\033[14;7H Comptes    ")())
    print((lambda: "\033[15;7H \033[31m Updates  \033[0m" if a==7 else "\033[15;7H Updates    ")())
    print((lambda: "\033[16;7H \033[31m Styles  \033[0m" if a==8 else "\033[16;7H Styles    ")())
    print((lambda: "\033[17;7H \033[31m Return Bug  \033[0m" if a==9 else "\033[17;7H Return Bug    ")())
    print((lambda: "\033[18;7H \033[31m Debug   \033[0m" if a==10 else "\033[18;7H Debug     ")())

ARKANTitleStyle = \
"\033[31m\033[7;47H█████  █████  █   █  █████  ██  █\n"+\
        "\033[8;47H█   █  █   █  █ ██   █   █  █ █ █\n"+\
        "\033[9;47H█████  ████   ██     █████  █ █ █\n"+\
       "\033[10;47H█   █  █ █    █ ██   █   █  █ █ █\n"+\
       "\033[11;47H█   █  █  ██  █   █  █   █  █  ██\n\
\033[12;47H" + version+ "\033[12;77H"+sysexp+"\033[0m" 

def AffichefenetreOptions():
    print("\
\033[3;5H┌─────────────────────┐\
\033[4;5H│ ╔═╗╔═╗╔╦╗╦╔═╗╔╗╦╔═╗ │\
\033[5;5H│ ║ ║╠═╝ ║ ║║ ║║║║╚═╗ │\
\033[6;5H│ ╚═╝╩   ╩ ╩╚═╝╩╚╝╚═╝ │\
\033[7;5H├─────────────────────┴" + "─"*94 + "┐")
    for i in range(20):
        print("\033["+str(8+i)+";5H│"+ " "*116 + "│")
    print("\033[28;5H"+"└"+ "─"*116 + "┘")


def AffichefenetreOptionsContols():
    print("\
\033[3;5H┌──────────────────────────┐\
\033[4;5H│ ╔═╗╔═╗╔╗╦╔╦╗╔═╗╔═╗╦  ╔═╗ │\
\033[5;5H│ ║  ║ ║║║║ ║ ╠╦╝║ ║║  ╚═╗ │\
\033[6;5H│ ╚═╝╚═╝╩╚╝ ╩ ╩╚ ╚═╝╚═╝╚═╝ │\
\033[7;5H├──────────────────────────┴" + "─"*89 + "┐")
    for i in range(20):
        print("\033["+str(8+i)+";5H│"+ " "*116 + "│")
    print("\033[28;5H"+"└"+ "─"*116 + "┘")


def PrintEcrandacceuil():
    print("\033[103m\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
                                                                                                                                \n\
\033[32m██████                                                                                                                          \n\
██████████                                                                                                                      \n\
████████████                                                                                                                    \n\
█████████████                                                                                                                   \n\
██████████████                                                                                                                  \n\
██████████████                                                                                                                  \n\
\033[44m███████████████                                                                                                                 \n\
████████████████                                                                                                                \n\
██████████████████                                                                                                              \n\
█████████████████████                                                                                                           \n\
████████████████████████                                                                                                        \n\
████████████████████████████████                                                                                                \n\
█████████████████████████████████████████████                                                                                   \n\
████████████████████████████████████████████████████████████                                                                    \n\
██████████████████████████████████████████████████████████████████████████████                                                  \n\
████████████████████████████████████████████████████████████████████████████████████████████████                                \n\
██████████████████████████████████████████████████████████████████████████████████████████████████████████                      \n\
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████             \n\
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████      \n\
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████   \n\
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████\n\
\033[42m\033[31mpip install ArkanYotaGame\033[32m███████████████████████████████████████████████████████████████████████████████████████████████████████\n\
\033[42m\033[31mhttps://github.com/ARKANYOTA/ArkanYotaGameCmd\033[32m██████████████████████████████████████████████████████████████\033[42m\033[31mCreated by Arkan Yota\033[0m", sep="", end="")
    print("\033[103m", ARKANTitleStyle,"\033[0m", sep="")
    
    
    
def VarSetMapDecor(mapx, mapy, loc):
    cls()
    for i in range(len(loc[mapx][mapy])): # 32 y
        print()
        for l in range(len(loc[mapx][mapy][i])): # 128 x
            a = loc[mapx][mapy][i][l]
            print((lambda: "\033[{0};{1}H".format(i+1, l+1)+" " if a=="0" else "")(),end="")
            print((lambda: "\033[{0};{1}H".format(i+1, l+1)+"█" if a=="1"else "")(),end="")
            print((lambda: "\033[{0};{1}H".format(i+1, l+1)+"V" if a=="!"else "")(),end="")
            print((lambda: "\033[{0};{1}H".format(i+1, l+1)+"X" if a=="*"else "")(),end="")
            print((lambda: "\033[{0};{1}H".format(i+1, l+1)+"\033[36m█\033[0m" if a=="b"else "")(),end="")
            print((lambda: "\033[{0};{1}H".format(i+1, l+1)+"?" if (a not in "0"+fullblock+InteractBlock) else "")(),end="")
            
def VarMessage(msg, x, y):
    if x < 64:      IsGauche = True;        px = x
    else:           IsGauche = False;       px = x-55
    if y < 16:      IsUp = True;            py = y
    else:           IsUp = False;           py = y-13
    
    try:
        if type(msg)==int:
            msg = msglist[msg]
    except IndexError:
        msg = "IndexError"
    except:
        msg = "à Simple Error"
    msg = msg.split("¶")
    cmdTrue = True
    while cmdTrue:
        if msg[0][0] == "$":
            command = msg[0]
            command = command[1:]
            exec(command)
            del msg[0]
        else:
            cmdTrue = False
    msgtimelist = []
    for a in msg:
        msgtimelist.append(a.split("µ"))
    msg = msgtimelist
    selectmsg = 0
    MsgTrue = True
    while MsgTrue:
        print("\033["+str(py+1)+";"+str(px+1)+"H╭","─"* 52,"╮",  sep="")
        for c in range(11):
            print("\033["+str(py+2+c)+";"+str(px+1)+"H│"," "* 52,"│",  sep="")
        print("\033["+str(py+13)+";"+str(px+1)+"H╰","─"* 52,"╯",  sep="")
        for msgfli in range(len(msg[selectmsg])):
            print("\033["+str(py+(5-(len(msg[selectmsg])//2))+msgfli)+";"+str(px+(27-(len(msg[selectmsg][msgfli])//2)))+"H",msg[selectmsg][msgfli], sep="")

        msgkey = getkey()
        CtrlC(msgkey)

        if msgkey == enter:
            if selectmsg+1<len(msg):
                selectmsg +=1
            else:
                break
        elif msgkey == openmsg or msgkey == escap:
            break
def cubeinventory(cubex, cubey, nb):
    print("\033["+str(cubey+0)+";"+str(cubex)+"H╭──╮",  sep="")
    print("\033["+str(cubey+1)+";"+str(cubex)+"H│\U0001f512│",  sep="")
    #print("\033["+str(cubey+2)+";"+str(cubex)+"H│  │",  sep="")
    if len(str(nb))==1:
        if nb==0:
            print("\033["+str(cubey+2)+";"+str(cubex)+"H╰──╯",  sep="")

        elif nb==1:
            print("\033["+str(cubey+2)+";"+str(cubex)+"H╰──╯",  sep="")
        else:
            print("\033["+str(cubey+2)+";"+str(cubex)+"H╰──",str(nb),  sep="")
    elif len(str(nb))==2:
        print("\033["+str(cubey+2)+";"+str(cubex)+"H╰─",str(nb),  sep="")
    else:
        print("\033["+str(cubey+2)+";"+str(cubex)+"H╰99+",  sep="")
        
def VarInventory(x,y):
    if x < 64:      IsGauche = True;        px = x
    else:           IsGauche = False;       px = x-55
    if y < 16:      IsUp = True;            py = y
    else:           IsUp = False;           py = y-13
    
    WhileInv = True
    while WhileInv:
        print("\033["+str(py+1)+";"+str(px+1)+"H╭","─"* 52,"╮",  sep="")
        for c in range(11):
            print("\033["+str(py+2+c)+";"+str(px+1)+"H│"," "* 52,"│",  sep="")
        print("\033["+str(py+13)+";"+str(px+1)+"H╰","─"* 52,"╯",  sep="")
        for i in range(4):
            for y in range(2):
                cubeinventory(px+3+(i*4), py+2+(y*3), 0)
        
        invkey = getkey()
        CtrlC(invkey)
        if invkey == enter:
            pass
        elif invkey == escap or invkey == invsee:
            break