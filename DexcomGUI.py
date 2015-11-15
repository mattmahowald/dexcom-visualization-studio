
"""
    author: Matt Mahowald
    last modified: November 2015
    website: https://github.com/mattmahowald/dexcom-vizualization-studio
"""

from tkinter import *
from tkinter.ttk import *

class Studio(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        # self.centerWindow()
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Dexcom Vizualizer Studio")
        self.style = Style()
        self.style.theme_use("aqua")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=50, y=50)

    def centerWindow(self):
      
        w = 1500
        h = 800

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
  
    root = Tk()
    root.geometry("1000x600+100+100")
    app = Studio(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  