import colorama
import shutil
import csv
import os



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


def add_task(a):
    with open("data.csv", mode='a', newline="") as file:
        ask = csv.writer()
        ask.writerow()
        print(colorama.Fore.GREEN+"added the")

add_task("make me a coffee")