from sys import platform
if platform[:3] == 'win':
    __keydict = {
        0x3b : 'f1',
        0x3c : 'f2',
        0x3d : 'f3',
        0x3e : 'f4',
        0x3f : 'f5',
        0x40 : 'f6',
        0x41 : 'f7',
        0x42 : 'f8',
        0x43 : 'f9',
        0x44 : 'f10',

        0x68 : 'altf1',
        0x69 : 'altf2',
        0x6a : 'altf3',
        0x6b : 'altf4',
        0x6c : 'altf5',
        0x6d : 'altf6',
        0x6e : 'altf7',
        0x6f : 'altf8',
        0x70 : 'altf9',
        0x71 : 'altf10',

        0x5e : 'ctrlf1',
        0x5f : 'ctrlf2',
        0x60 : 'ctrlf3',
        0x61 : 'ctrlf4',
        0x62 : 'ctrlf5',
        0x63 : 'ctrlf6',
        0x64 : 'ctrlf7',
        0x65 : 'ctrlf8',
        0x66 : 'ctrlf9',
        0x67 : 'ctrlf10',

        0x54 : 'shiftf1',
        0x55 : 'shiftf2',
        0x56 : 'shiftf3',
        0x57 : 'shiftf4',
        0x58 : 'shiftf5',
        0x59 : 'shiftf6',
        0x5a : 'shiftf7',
        0x5b : 'shiftf8',
        0x5c : 'shiftf9',
        0x5d : 'shiftf10',

        0x52 : 'ins',
        0x53 : 'del',
        0x4f : 'end',
        0x50 : 'down',
        0x51 : 'pgdn',
        0x4b : 'left',
        0x4d : 'right',
        0x47 : 'home',
        0x48 : 'up',
        0x49 : 'pgup',
        
        0xa2 : 'altins',
        0xa3 : 'altdel',
        0x9f : 'altend',
        0xa0 : 'altdown',
        0xa1 : 'altpgdn',
        0x9b : 'altleft',
        0x9d : 'altright',
        0x97 : 'althome',
        0x98 : 'altup',
        0x99 : 'altpgup',

        0x92 : 'ctrlins',
        0x93 : 'ctrldel',
        0x75 : 'ctrlend',
        0x91 : 'ctrldown',
        0x76 : 'ctrlpgdn',
        0x73 : 'ctrlleft',
        0x74 : 'ctrlright',
        0x77 : 'ctrlhome',
        0x8d : 'ctrlup',
        0x84 : 'ctrlpgup',

        3 : 'ctrl2'
    }

    import ctypes
    import msvcrt
    
    def getch():
        n = ord(ctypes.c_char(msvcrt.getch()).value)
        try:
            c = chr(n)
        except:
            c = '\0'
        return (n, c)

    def getkey():
        n, c = getch()
        # 0xE0 is 'grey' keys.  change this if you don't like it, but I don't care what color the key is.  IMHO it just confuses the end-user if they need to know.
        if n == 0 or n == 0xE0:
            n, c = getch()
            if n in __keydict:
                return __keydict[n]
            return "key%x" % n
        return c
    
elif platform[:3] == 'lin' or platform[:3] == 'dar':
    import tty
    import termios
    from sys import stdin
    def getch():
        fd = stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(stdin.fileno())
            ch = stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def getkey():
        getchar = getch
        c1 = getchar()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5b:
            return c1 + c2
        c3 = getchar()
        if ord(c3) != 0x33:
            return c1 + c2 + c3
        c4 = getchar()
        return c1 + c2 + c3 + c4
