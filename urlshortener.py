import pyshorteners
from termcolor import colored
import os
import ctypes
import time

ctypes.windll.kernel32.SetConsoleTitleW("url shortener")

os.system("cls")

work = True

while work==True:
    os.system("cls")
    print(colored("""
    ██╗░░░██╗██████╗░██╗░░░░░  ░██████╗██╗░░██╗░█████╗░██████╗░████████╗███████╗███╗░░██╗███████╗██████╗░
    ██║░░░██║██╔══██╗██║░░░░░  ██╔════╝██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗░██║██╔════╝██╔══██╗
    ██║░░░██║██████╔╝██║░░░░░  ╚█████╗░███████║██║░░██║██████╔╝░░░██║░░░█████╗░░██╔██╗██║█████╗░░██████╔╝
    ██║░░░██║██╔══██╗██║░░░░░  ░╚═══██╗██╔══██║██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██║╚████║██╔══╝░░██╔══██╗
    ╚██████╔╝██║░░██║███████╗  ██████╔╝██║░░██║╚█████╔╝██║░░██║░░░██║░░░███████╗██║░╚███║███████╗██║░░██║
    ░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

    """, 'blue'))

    url = input("enter the url: ")

    shortener = pyshorteners.Shortener()
    shorturl = shortener.tinyurl.short(url)

    print(shorturl)

    end = input("""
do you want continue in this program?(y/n): """)


    if (end == "y"):
        continue

    elif (end == "n"):
        print("program ended")
        time.sleep(2)
        exit()
