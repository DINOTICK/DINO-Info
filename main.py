from Infogather import System_information
import tkinter as tk
import tkinter.font as tkFont
import platform
import socket
import uuid
import re
import psutil

class App:
    def __init__(self, root):
        #setting title
        uname = platform.uname()
        root.title("System Info")
        #setting window size
        width=237
        height=355
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_608=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_608["font"] = ft
        GLabel_608["fg"] = "#333333"
        GLabel_608["bg"] = "#999999"
        GLabel_608["justify"] = "center"
        GLabel_608["text"] = "System Info"
        GLabel_608["relief"] = "sunken"
        GLabel_608.place(x=20,y=0,width=190,height=35)

        GLabel_171=tk.Label(root)
        GLabel_171["activebackground"] = "#606060"
        GLabel_171["activeforeground"] = "#737373"
        GLabel_171["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_171["font"] = ft
        GLabel_171["fg"] = "#999999"
        GLabel_171["justify"] = "center"
        GLabel_171["text"] = ""
        GLabel_171["relief"] = "ridge"
        GLabel_171.place(x=20,y=30,width=190,height=3)

        GLabel_527=tk.Label(root)
        GLabel_527["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=23)
        GLabel_527["font"] = ft
        GLabel_527["fg"] = "#333333"
        GLabel_527["justify"] = "center"
        GLabel_527["text"] = "Machine Info"
        GLabel_527["relief"] = "sunken"
        GLabel_527.place(x=0,y=50,width=235,height=30)

        GLabel_151=tk.Label(root)
        GLabel_151["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_151["font"] = ft
        GLabel_151["fg"] = "#333333"
        GLabel_151["justify"] = "center"
        GLabel_151["text"] = f"Machine: {uname.machine}"
        GLabel_151["relief"] = "ridge"
        GLabel_151.place(x=0,y=80,width=235,height=30)

        GLabel_284=tk.Label(root)
        GLabel_284["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_284["font"] = ft
        GLabel_284["fg"] = "#333333"
        GLabel_284["justify"] = "center"
        GLabel_284["text"] = f"Processor: {uname.processor}"
        GLabel_284["relief"] = "ridge"
        GLabel_284.place(x=0,y=110,width=235,height=30)

        GLabel_371=tk.Label(root)
        GLabel_371["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_371["font"] = ft
        GLabel_371["fg"] = "#333333"
        GLabel_371["justify"] = "center"
        GLabel_371["text"] = f"System: {uname.system}"
        GLabel_371["relief"] = "ridge"
        GLabel_371.place(x=0,y=140,width=235,height=30)

        GLabel_323=tk.Label(root)
        GLabel_323["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=23)
        GLabel_323["font"] = ft
        GLabel_323["fg"] = "#333333"
        GLabel_323["justify"] = "center"
        GLabel_323["text"] = "Network Info"
        GLabel_323["relief"] = "sunken"
        GLabel_323.place(x=0,y=170,width=235,height=30)

        GLabel_960=tk.Label(root)
        GLabel_960["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_960["font"] = ft
        GLabel_960["fg"] = "#333333"
        GLabel_960["justify"] = "center"
        GLabel_960["text"] = f"Ip-Address: {socket.gethostbyname(socket.gethostname())}"
        GLabel_960["relief"] = "ridge"
        GLabel_960.place(x=0,y=200,width=235,height=30)

        GLabel_367=tk.Label(root)
        GLabel_367["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}"
        GLabel_367["relief"] = "ridge"
        GLabel_367.place(x=0,y=230,width=235,height=30)

        GLabel_375=tk.Label(root)
        GLabel_375["bg"] = "#999999"
        ft = tkFont.Font(family='Times',size=23)
        GLabel_375["font"] = ft
        GLabel_375["fg"] = "#333333"
        GLabel_375["justify"] = "center"
        GLabel_375["text"] = "Resource Info"
        GLabel_375["relief"] = "sunken"
        GLabel_375.place(x=0,y=260,width=235,height=30)

        GLabel_175=tk.Label(root)
        GLabel_175["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_175["font"] = ft
        GLabel_175["fg"] = "#333333"
        GLabel_175["justify"] = "center"
        GLabel_175["text"] = f"Total CPU Usage: {psutil.cpu_percent()}%"
        GLabel_175["relief"] = "ridge"
        GLabel_175.place(x=0,y=290,width=235,height=30)

        GLabel_635=tk.Label(root)
        GLabel_635["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_635["font"] = ft
        GLabel_635["fg"] = "#333333"
        GLabel_635["justify"] = "center"
        svmem = psutil.virtual_memory()
        GLabel_635["text"] = f"Percentage: {svmem.percent}%"
        GLabel_635["relief"] = "ridge"
        GLabel_635.place(x=0,y=320,width=235,height=30)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
