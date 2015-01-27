import curses
import curses.textpad
import time

#Load some sound
import pygame
import base64

import controller

GNDSTR = "~~^~~"

BGSTR = ["  >^<                 /\                      ",
         "                     /# \            \./      ",
         "                    /### \    /\              ",
         "        ~^~        /   ###\  /##\             " , 
         "    /\            /    ## #\/##\/\            " ,
         "   /# \          / /  /      /# /#\           ",
         "  /  ##\  /\/// //  /\  /    _/  /#\          ",
         " /###   \#  //  /  /  \     / /    #\/\   /\  ",
         "/ //###  \# \/    / ## \   / /   _  /  \ /# \ ",
         "`--`~~--`-`-== `-`= == ~~ -=`=-`````~- == ==` " ]


SPASH = [" __    __       ___      ___   ___   ___   .______            ",
         "|  |  |  |     /   \     \  \ /  /  / _ \  |   _  \           ",
         "|  |__|  |    /  ^  \     \  V  /  | | | | |  |_)  |          ",
         "|   __   |   /  /_\  \     >   <   | | | | |      /           ",
         "|  |  |  |  /  _____  \   /  .  \  | |_| | |  |\  \----.      ",
         "|__|  |__| /__/     \__\ /__/ \__\  \___/  | _| `._____|      ",
         "                                                              ",
         ".___________.  ______     ______    __  ___  __  .___________.",
         "|           | /  __  \   /  __  \  |  |/  / |  | |           |",
         "`---|  |----`|  |  |  | |  |  |  | |  '  /  |  | `---|  |----`",
         "    |  |     |  |  |  | |  |  |  | |    <   |  |     |  |     ",
         "    |  |     |  `--'  | |  `--'  | |  .  \  |  |     |  |     ",
         "    |__|      \______/   \______/  |__|\__\ |__|     |__|     ",
         "                                                              ",
         "                                                  By Dang42   "]



HELOA = [" L                             ",
         "LOL    ROFL:ROFL:LOL:ROFL:ROFL ",
         " L\\          ____I_____       ",
         "    ==========    |   |[\      ",
         "              \___|0==___)     ",
         "              ___I__I__/       ",
         ]

HELOB = ["L L                           ",
         " O              :LOL:         ",
         "L L\          ____I_____      ",
         "    ==========    |   |[\     ",
         "              \___|0==___)    ",
         "              ___I__I__/      ",
         ]


HELOC = [" L                               ",
         "LOL  HaXor:HaXor:LOL:HaXor:HaXor ",
         " L\\          ____I_____         ",
         "    ==========    |   |[\        ",
         "              \___|0==___)       ",
         "              ___I__I__/         ",
         ]




HOUSES = ["               /-------\      ",
          "   /-----\     | [] [] |      ",
          "   |[] []|     | [] [] |      ",
          "~~~+~~~~~+~~~~~+~~~~~~~+~~~~~~"]

class theview(object):
    """Main Meiw object"""
    def __init__(self):
        """Create the main window"""
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(1)
        #Init mixer

        #Init Colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

        pygame.mixer.init()



        self.helopos = None
        self.screen = screen
        self.xpos = 0

        self.splashscreen()

        #pygame.mixer.music.stop()


        self.mainmenu()
        #pygame.mixer.music.stop()

        curses.endwin()


    def splashscreen(self):
        screen = self.screen

        mid_file = "nevergon_rickashley.mid"
        pygame.mixer.music.load(mid_file)
        pygame.mixer.music.play()

        screen.border(0)
        idx = 5
        for line in SPASH:
            screen.addstr(idx,5, line)
            idx += 1

        screen.addstr(20,5,"Press Space to l33t Hax", curses.A_REVERSE)

        screen.nodelay(1)

        while 1:
            c = screen.getch()
            if c == ord(" "):
                pygame.mixer.music.stop()
                return

            elif c == ord("z"):
                sys.exit(0)
            time.sleep(1)
            #curses.flash()


    def mainmenu(self):
        """Show the main menu"""
        screen = self.screen
        paused = True
        #Outer loop to show the menu


        mid_file = "rvalkyri.mid"
        pygame.mixer.music.load(mid_file)


        while True:
            screen.clear()
            screen.border(0)
            screen.addstr(0,0,"Main Menu")

            #And do the prompts
            screen.addstr(5,5, "1) Scan Port")
            screen.addstr(6,5, "2) Lookup Mac")
            screen.addstr(7,5, "3) Crack House")
            screen.addstr(8,5, "4) List Restricted")
            screen.addstr(9,5, "5) Awesome Mode!!")
            screen.addstr(10,5, "q) quit")

            #Create a subwindow
            while 1:
                c = screen.getch()
                if c == ord('q'):
                    return
                elif c == ord('1'):
                    self.scanport()
                    break
                elif c == ord('2'):
                    self.doOUI()
                    break
                elif c == ord('3'):
                    self.crackhouse()
                    break
                elif c == ord('4'):
                    self.listrestricted()
                    break
                elif c == ord('5'):
                    #Toggle Awesome Mode
                    if paused:
                        pygame.mixer.music.play()
                        paused = False
                        self.animatehelo()
                        screen.nodelay(1)
                    else:
                        pygame.mixer.music.stop()
                        paused = True
                        screen.nodelay(0)
                    break
                else:
                    if not paused:
                        self.animatehelo()
                time.sleep(0.1)

    def scanport(self):
        screen = self.screen
        screen.nodelay(0)

        win = curses.newwin(40,80,0,0)
        win.clear()
        win.border()
        win.addstr("Scan Ports")
        win.keypad(1)
        dohttp = False
        dossh = False
        dotelnet = False
        hostaddress = None

        haserror = False

        cpos = 3
        #Add the options
        while True:
            #First lets do the Services
            win.clear()
            win.border()
            win.addstr("Scan Ports")
            win.addstr(2,5,"SERVICES", curses.A_UNDERLINE)
            win.addstr(3,5,"HTTP   [ ]")
            win.addstr(4,5,"SSH    [ ]")
            win.addstr(5,5,"TELNET [ ]")

            #Process the checkboxes
            if dohttp:
                win.addstr(3,13,"X")
            if dossh:
                win.addstr(4,13,"X")
            if dotelnet:
                win.addstr(5,13,"X")

            win.addstr(7,5,"HOST:",curses.A_UNDERLINE)
            win.addstr(7,13," "*40,curses.A_UNDERLINE)

            if hostaddress:
                win.addstr(7,13,hostaddress,curses.A_UNDERLINE)

            if haserror:
                win.addstr(9,5,haserror, curses.A_STANDOUT)

            win.addstr(20,5,"Arrows to move")
            win.addstr(21,5,"Space to enter details")
            win.addstr(22,5,"s to start scan")
            win.addstr(23,5,"q to return to main")
            win.move(cpos,13)
            #Move the cursor to the start
            ch =win.getch()
            if ch == ord('q'):
                del(win)
                return
            elif ch == curses.KEY_DOWN:
                if cpos < 5:
                    cpos += 1
                elif cpos == 5:
                    cpos = 7
                win.move(cpos,13)
            elif ch == curses.KEY_UP:
                if cpos == 7:
                    cpos = 5
                elif cpos >= 3:
                    cpos -= 1
                win.move(cpos,13)
            elif ch == ord(' '):
                if cpos == 3:
                    #Check box on http
                    dohttp = not dohttp
                elif cpos == 4:
                    dossh = not dossh
                elif cpos == 5:
                    dotelnet = not dotelnet
                elif cpos == 7:
                    win.addstr(7,13," "*40,curses.A_UNDERLINE)
                    win.move(cpos,13)
                    win.refresh()
                    curses.echo()
                    hostaddress = win.getstr()
                    curses.noecho()
            elif ch == ord('s'):
                #DO the magics
                if not (dohttp or dossh or dotelnet):
                    haserror = "No Service Selected"
                    if not hostaddress:
                        haserror = "No Service or Hostname Given"
                elif not hostaddress:
                    haserror = "No Hostname given"
                else:
                    output = controller.scanports(hostaddress,
                                                  dohttp,
                                                  dossh,
                                                  dotelnet)

                    #Output Header
                    header, results = output #Break this down
                    win.addstr(12, 5, header)
                    idx = 13

                    for line in results:
                        win.addstr(idx,5,"Port {0} ({1}):\t{2}".format(line[0],
                                                                       line[1],
                                                                       line[2]))
                        idx += 1
                    #Any Key
                    win.addstr(20, 5, "Any key to continue")
                    #Clear the input bit
                    for idx in range(21,25):
                        win.addstr(idx,0," "*50)
                    win.getch()
                    return

    def listrestricted(self):
        """Window for the list restricted function"""
        screen = self.screen
        screen.nodelay(0)

        win = curses.newwin(40,80,0,0)
        win.keypad(1)
        curses.noecho()

        site = "www.google.com"

        cpos = 3

        while True: #Loop to update window
            win.clear()
            win.border(0)
            win.addstr("List Restricted")

            #And the checkbox part
            win.addstr(2,5,"SCAN", curses.A_UNDERLINE)
            win.addstr(3,5,"google   [ ]")
            win.addstr(4,5,"yahoo    [ ]")
            win.addstr(5,5,"coventry [ ]")
            win.addstr(6,5,"Other")
            win.addstr(6,15," "*30, curses.A_UNDERLINE)
            #Draw Selected box bits
            if site == "www.google.com":
                win.addstr(3,15,"X")
            elif site == "www.yahoo.com":
                win.addstr(4,15,"X")
            elif site == "www.coventry.ac.uk":
                win.addstr(5,15,"X")
            else:
                win.addstr(6,15,site)

            #Navigation

            win.addstr(20,5,"Arrows to move")
            win.addstr(21,5,"Space to Toggle")
            win.addstr(22,5,"s to start scan")
            win.addstr(23,5,"q to return to main")
            win.move(cpos,15)
            win.refresh()
            ch = win.getch()
            if ch == ord('q'):
                return
            elif ch == ord("s"):
                #Do the output bit
                lines = controller.listrestricted(site)

                idx = 9
                win.addstr(8,5,"Restricted for {0}".format(site))
                for line in lines:
                    win.addstr(idx,9,line)
                    idx += 1
                win.getch()
                return

            elif ch == curses.KEY_UP:
                if cpos >= 3:
                    cpos -= 1
            elif ch == curses.KEY_DOWN:
                if cpos <= 6:
                    cpos += 1
            elif ch == ord(' '):
                #toggle based on position
                if cpos == 3:
                    site = "www.google.com"
                elif cpos == 4:
                    site = "www.yahoo.com"
                elif cpos == 5:
                    site = "www.coventry.ac.uk"
                elif cpos == 6:
                    curses.echo()
                    site = win.getstr()
                    curses.noecho()



    def doOUI(self):
        screen = self.screen
        screen.nodelay(0)
        win = curses.newwin(40,80,0,0)

        win.clear()
        win.border(0)
        curses.echo() #Allow inout to be shown
        win.addstr(2,5, "MAC Address:")
        #And a box for this input
        win.addstr(2,20, "_"*30, curses.A_UNDERLINE)
        win.move(2,21) #Move cursor to start
        win.refresh()

        macadd = win.getstr()
        curses.noecho()

        #And run the mac lookup
        vendor = controller.lookupmac(macadd)

        if not vendor:
            win.addstr(4,5, "No Match in database")
        else:
            win.addstr(4,5, "Manufacturer is {0}".format(vendor))

        win.addstr(10,5, "Press any key to continue")
        #while 1:
        ch = win.getch()
        print "CHAR GOT"
        del(win)

        #if ch == ord("x"):
        return

        # #Work out input
        # ch = screen.getch()
        # print ch
        # return
        # #screen.addstr(0,0, "Identify OUI")
        # #
        # #screen.addstr(2,5, "Enter Mac Address")
        # #textpad = curses.textpad.Textbox()

    def crackhouse(self):
        screen = self.screen
        win = curses.newwin(40,80,0,0)

        badinput = False
        startpin = None
        endpin = None

        #Process input
        win.clear()
        win.border(0)
        curses.echo() #Display input
        win.addstr("Crack House")
        #For fun we could add some imput

        win.addstr(5,5,"Starting Pin:")
        win.addstr(5,20, "_"*30, curses.A_UNDERLINE)

        win.addstr(6,5,"Ending Pin  :")
        win.addstr(6,20, "_"*30, curses.A_UNDERLINE)

        win.move(2,20) #Move cursor to start

        #Do the input part
        while True:
            win.addstr(5,5,"Starting Pin:")
            win.addstr(5,20, "_"*30, curses.A_UNDERLINE)

            if badinput:
                win.addstr(10,5,badinput)

            win.move(5,20) #Move cursor to start
            thepin = win.getstr()
            try:
                startpin = int(thepin)
                badinput = None
                break
            except ValueError:
                badinput = "Starting pin must be an Integer"

        #Do the input part for second pin
        while True:
            win.addstr(6,5,"Ending Pin  :")
            win.addstr(6,20, "_"*30, curses.A_UNDERLINE)

            if badinput:
                win.addstr(10,5,badinput)

            win.move(6,20) #Move cursor to start
            thepin = win.getstr()
            try:
                endpin = int(thepin)
                if endpin <= startpin:
                    badinput = "Ending pin mut be > starting pin"
                else:
                    badinput = None
                    break
            except ValueError:
                badinput = "Ending pin must be an Integer"

        curses.noecho()
        win.addstr(10,5," "*50) #Remove any errors
        win.addstr(10,5,"Cracking house for pins {0}-{1}".format(startpin,
                                                                 endpin))

        #Work out status bar
        statusstart = 5 #Start point
        statuslen = 70  #Total Length

        percentjump = 100 / (endpin - startpin)
        currentpercent = 0

        #Draw the status bar:
        for x in range(startpin,endpin):
            win.addstr(11,5,"Checking {0}".format(x))
            win.addstr(12,5," "*statuslen, curses.A_STANDOUT)
            #Work out lenght of complete bar
            barlen = int(statuslen * (currentpercent / 100.0))
            win.addstr(12,5,"#"*barlen, curses.A_STANDOUT)
            #Add the percentage
            win.addstr(12,5+(statuslen/2)-2,"{0} %".format(currentpercent))
            currentpercent += percentjump
            win.refresh()

            #The Crack itself
            hasmatch = controller.cracksingle(x)
            if hasmatch:
                win.addstr(15,5, "Pin Match found: {0}".format(x))
                win.addstr(16,5, "Any key to exit")
                ch = win.getch()
                return

        win.addstr(15,5, "No Match Found :(")
        win.addstr(16,5, "Any key to exit")
        ch = win.getch()
        return

    def animatehelo(self):
        screen = self.screen
        maxsize = screen.getmaxyx()
        
        #Draw some ground
        #A pad for the main data

        gidx = 10 # Grab from a global

        thepad = curses.newpad(10,maxsize[1]+40) #Add 20 at each end
        thepad.refresh(0,20,12,0,25,79) #Px, Py, #(winx start) #(win y start),  XY End Start - 20 from start)
        while True:
            
            #thepad.addstr(0,gidx,"{0}{1}{0}".format("-"*20,maxsize))
            #thepad.addstr(9,gidx,"{0}{1}{2}{1}{0}".format("+","-"*19,"="*40))

            #Do the Ground effect
            thepad.addstr(9,gidx,"{0}".format("--^--"*18)) #80 / 5 + 10

        #thewin = curses.newwin(2, maxsize[1])
        #thewin.addstr(1,0,"{0}{1}{0}".format("-"*20,"="*20))
        #thewin.refresh()


            thepad.refresh(0,20,12,0,25,79) #Px, Py, #(winx start) #(win y start),  XY End Start - 20 from start)
            #thepad.refresh(0,0,12,0,25,79) #Px, Py, #(winx start) #(win y start),  XY End
        
            val =thepad.getch()
            if val == ord('q'):
                sys.exit(0)

            gidx -= 1            
            if gidx < 0:
                gidx = 10

        #thewin = curses.newwin(10,20)
        #thewin.addstr(0,5,"=-"*10)

        #thewin.overlay(thepad)
        #Overlay this window on the pad
        #thepad.overlay(thewin)

    #def oldhelo(self)
    def animatehelo2(self):
        #maxsize = foo.getmaxyx()

        screen = self.screen
        maxsize = screen.getmaxyx()
        loopsize = maxsize[1]+35
        win = curses.newpad(10,maxsize[1]+40)

        #Work out how big we want the "ground" window to be
        #Add 1 to give a bit of breathing space
        #gndloops = (maxsize[1] / len(GNDSTR)) +1
        #gndsize = maxsize[1] * gndloops

        #winGnd = curses.newpad(10, gndsize)

        #Sort the ground
        #winGnd.addstr(8,0, GNDSTR * groundloops)

        #win.box()
        xpos = self.xpos # Base for parralax
        hpos = self.helopos

        #Work out scroll
        

        if hpos is None:
            hpos = loopsize
        elif hpos == 0:
            hpos = loopsize

        if xpos % 2 == 0:
            hpos -= 1

        #Work out the size of the loop for the houses
        housesize = len(HOUSES[0])
        totallines = loopsize/housesize
        

        if hpos % 3 == 0:
            thesprite = HELOA
        elif hpos % 2 == 0:
            thesprite = HELOB
        else:
            thesprite = HELOC


        idx = 1
        for line in thesprite:
            win.addstr(idx,maxsize[1], line, curses.color_pair(1))
            idx +=1



        #xpos +=1

        #win.addstr(0,0,"{0} {1} {2}".format(hpos,maxsize[0], maxsize[1]))
        self.helopos = hpos

        win.refresh(0,hpos,12,0,25,79)  #Do the Base
        
        screen.refresh()
       


if __name__ == "__main__":
    theview()
    #try:
    #    theview()
    #except Exception,e:  #Bad form but what the hell
    #    curses.endwin()
    #    print "ERROR:"
    #    print e

    curses.endwin()
