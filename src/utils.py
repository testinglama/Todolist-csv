import colorama
import shutil
import csv
import os
import time



def banner():
    art = r"""

█████  ███  ████   ███       █     ███  ████ █████ 
  █   █   █ █   █ █   █      █      █  █       █   
  █   █   █ █   █ █   █ ████ █      █   ███    █   
  █   █   █ █   █ █   █      █      █      █   █   
  █    ███  ████   ███       █████ ███ ████    █   

 """
    cmd_width = shutil.get_terminal_size().columns
    lines = art.splitlines()
    for line in lines:
        print(line.center(cmd_width))


def loading_scr(x = 5):
    tme = time.time()
    while time.time() - tme < x:
        for dot in range(4):
            print( f"\rloading{'.' * dot:<3}", end="", flush=True)
