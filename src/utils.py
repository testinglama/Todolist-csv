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
        print(colorama.Fore(line.center(cmd_width)))



