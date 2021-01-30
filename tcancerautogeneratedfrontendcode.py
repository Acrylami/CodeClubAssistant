import tkinter as tk
import tkinter.font as tkFont



class App:
    def __init__(self, root):
        #setting title
        root.title("Athena")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_984=tk.Label(root)
        ft = tkFont.Font(family='Times',size=60)
        GLabel_984["font"] = ft
        GLabel_984["fg"] = "#333333"
        GLabel_984["justify"] = "center"
        GLabel_984["text"] = "Athena"
        GLabel_984.place(x=0,y=0,width=240,height=67)

        GLabel_69=tk.Label(root)
        ft = tkFont.Font(family='Times',size=36)
        GLabel_69["font"] = ft
        GLabel_69["fg"] = "#333333"
        GLabel_69["justify"] = "center"
        GLabel_69["text"] = "Athena says:"
        GLabel_69.place(x=140,y=110,width=302,height=59)

        GLabel_835=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_835["font"] = ft
        GLabel_835["fg"] = "#333333"
        GLabel_835["justify"] = "center"
        GLabel_835["text"] = "Start Athena to use"
        GLabel_835.place(x=10,y=170,width=572,height=264)

        GButton_604=tk.Button(root)
        GButton_604["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=24)
        GButton_604["font"] = ft
        GButton_604["fg"] = "#000000"
        GButton_604["justify"] = "center"
        GButton_604["text"] = "Start Athena"
        GButton_604.place(x=10,y=440,width=574,height=51)
        GButton_604["command"] = self.GButton_604_command

    def GButton_604_command(self):
        print("command")

root = tk.Tk()
app = App(root)

root.mainloop()
