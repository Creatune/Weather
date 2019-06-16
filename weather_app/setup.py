import os
import tkinter as tk
from tkinter import messagebox
import time

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
message_box('','This programme will install a few python modules to run the weather app successfully')
time.sleep(2)

message_box('','Your download will start now')

os.system('sudo apt-get install python3')
os.system('sudo apt-get install python3-pip')
os.system('pip3 install requests')

message_box('Finished!','The installation has finished. Run the program.py file to see if the weather app works.')
