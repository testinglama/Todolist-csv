import colorama
import time 
import shutil as sh
import random as rd
import csv
import utils as ut
import os

#=============>TODO LIST<===================
print(colorama.Fore.RED+colorama.Style.BRIGHT)

ut.banner()
print(colorama.Fore.WHITE)
print("\n")
print(colorama.Fore.LIGHTMAGENTA_EX+colorama.Style.BRIGHT+"     HELLO USER WELCOME TO TODO-LIST  :  "+"\n\n")

if not os.path.exists("D:\sheet_cleaner\todolist\Todolist-csv\data"):
    print("unable to proceed further")

while True:
    print("     OPTIONS ARE :    "+colorama.Fore.YELLOW)
    print("ADD TASK : (1)\n")
    print("REMOVE TASK : (2)\n")
    print("EDIT TASK : (3)\n")

    inp = input("WRITE YOUR CHOICE ")

    if inp == "":
        print("\nexiting the app...\n")
        time.sleep(1.5)
        print("\nexited the app!\n")
        break

    if inp == "1":
        print(colorama.Style.DIM+" OPENING ADD TASK TERMINAL: ")

        ut.loading_scr(2)
        tsk = input("\nenter your task\n")
        with open("data", mode="a", newline="",encoding="utf-8") as file:
            wrte = csv.writer(file)
            if not tsk:
                print("\ncannot save empty inputs\n")
                continue
            wrte.writerow(tsk)

        










