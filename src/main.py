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
print("     OPTIONS ARE :    "+colorama.Fore.YELLOW)

print("ADD TASK : (1)\n")
print("REMOVE TASK : (2)\n")
print("EDIT TASK : (3)\n")

try:
    inp = int(input("WRITE YOUR CHOICE "))
except:
    print(colorama.Fore.RED+"some error occured"+ colorama.Fore.WHITE)





