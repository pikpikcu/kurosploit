#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import os,sys
import time
from time import sleep
from os import system
from colors import bcolors
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End

    
banner1 ="""\033[1;32m
                                                                         
_|    _|                                                    _|            _|    _| 
_|  _|    _|    _|  _|  _|_|    _|_|      _|_|_|  _|_|_|    _|    _|_|       _|_|_|_|   
_|_|      _|    _|  _|_|      _|    _|  _|_|      _|    _|  _|  _|    _|  _|    _| 
_|  _|    _|    _|  _|        _|    _|      _|_|  _|    _|  _|  _|    _|  _|    _| 
_|    _|    _|_|_|  _|          _|_|    _|_|_|    _|_|_|    _|    _|_|    _|     _|_| 
                                                  _|             
                                                  _|                                       
                           

\033[1;m"""

banner2 ="""\033[31m
   __   __)                              
  (, ) /                      /)    ,    
    /(       __  ___ _  __   // ___  _/_ 
 ) /  \_(_(_/ (_(_) /_)_/_)_(/_(_)_(_(__ 
(_/                  .-/                
                    (_/                   
                 
\033[1;m"""
banner3 =bcolors.cyan+"""
▄ •▄ ▄• ▄▌▄▄▄        .▄▄ ·  ▄▄▄·▄▄▌        ▪  ▄▄▄▄▄
█▌▄▌▪█▪██▌▀▄ █·▪     ▐█ ▀. ▐█ ▄███•  ▪     ██ •██  
▐▀▀▄·█▌▐█▌▐▀▀▄  ▄█▀▄ ▄▀▀▀█▄ ██▀·██▪   ▄█▀▄ ▐█· ▐█.▪
▐█.█▌▐█▄█▌▐█•█▌▐█▌.▐▌▐█▄▪▐█▐█▪·•▐█▌▐▌▐█▌.▐▌▐█▌ ▐█▌·
·▀  ▀ ▀▀▀ .▀  ▀ ▀█▄▀▪ ▀▀▀▀ .▀   .▀▀▀  ▀█▄▀▪▀▀▀ ▀▀▀   
                
\033[1;m"""
stream = (banner1, banner2,banner3)
def banner():
	print random.choice(stream)

def _etc_():
    print ""+N+"         =[ "+O+"KuroSploit v0.1[Beta] "+N+"]"
    print "  + -- --=[ "+R+"github:pikpikcu "+N+"]"
def cls():
    system('clear')
def exits():
    def exit(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random() * 0.9)
    print""+G+""
    sleep(0.4)
    print""+B+""
    exit('--[+] Thanks for using KuroSploit [+]--')
    print""+R+""
