import colorama
import shutil



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



def first_msg():
    return("\n\n"+colorama.Style.BRIGHT+"WELCOME TO THE TODO LIST")
