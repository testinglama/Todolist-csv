import colorama
import time 
import shutil as sh
import random as rd
import csv
import utils as ut

#=============>TODO LIST<===================
print(colorama.Fore.RED+colorama.Style.BRIGHT)

ut.banner()
print(colorama.Fore.WHITE)
print("\n")
print(colorama.Fore.LIGHTMAGENTA_EX+colorama.Style.BRIGHT+"     HELLO USER WELCOME TO TODO-LIST  :  "+"\n\n")

ask_task = input("write the task you want to add in todo list")

ut.add_task(ask_task)



while True:
    print("     OPTIONS ARE :    "+colorama.Fore.YELLOW)
    print("ADD TASK : (1)\n")
    print("REMOVE TASK : (2)\n")
    print("EDIT TASK : (3)\n")

    inp = input("WRITE YOUR CHOICE ")

    if inp == "" or str :
        print("\nexiting the app...\n")
        time.sleep(1.5)
        print("\nexited the app!\n")
        break










