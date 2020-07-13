#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os,sys
import etc
from time import sleep
from kurosploit import *
from os import popen,system 
from etc.colors import bcolors
from etc.banner import (banner,\
                       _etc_,\
                       cls)
id = popen('whoami').read()
#if not os.geteuid() == 0:#Detected user root
#       cls()
#       sys.exit(bcolors.white+"\n["+bcolors.red+"!"+bcolors.white+"]"+bcolors.green+" Please run kurosPloit as root!!.\n" )
if __name__ == "__main__" or cls() or banner() or _etc_():
    main()
def main():
            try:
                CMD = raw_input("\n"+bcolors.pink+"┌──<{0}└──╼>kurosPloit>> ".format(id).lower()+bcolors.lightcyan)
                if str(CMD) == 'use listener':
                    etc.menu.listener()
                    main()
                elif str(CMD) == 'use backdoor':
                    etc.menu.malware()
                elif str(CMD) == 'show modules':
                    etc.help.modules()
                    main()
                elif str(CMD) =='show options':
                    etc.help.help()
                    main()
                elif str(CMD) =='banner':
                    cls()
                    banner(),_etc_(),main()
                elif str(CMD) =='clear':
                    cls()
                    main()
                elif str(CMD) =='exit':
                    etc.banner.exits()
                    exit()
                else:
                    print "Wrong Command => ", str(CMD)
                    print ""+bcolors.lightcyan+""+bcolors.blue+"["+bcolors.red+"!"+bcolors.blue+"] "+bcolors.white+"Please enter 'show options'"
                    main()
            except(KeyboardInterrupt):
                print"\n"+bcolors.red+"[*] (Ctrl + C ) Detected, Trying To Exit ...\n" 
                sleep(2)
                print""+bcolors.green+"[*] Thank You For Using KuroSploit =)\n" 
                sleep(3)
                exit()
