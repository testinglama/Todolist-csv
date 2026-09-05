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

file_path = os.path.isfile("data.csv")

def new_task():
    with open(data.csv, mode="a",newline="", encoding="utf8"):
    ask = input("what is the task you want to add")
    read = csv