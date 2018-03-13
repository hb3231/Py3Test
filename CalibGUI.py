#Simple GUI

from tkinter import *
class Application(Frame):
    """ A GUI application  """
    def __init__(self, master):
        """ init the frame"""
        Frame._init_(self, master)
        self.grid()
        self.button_clicks = 0 #count the button clicks
	    self.create_widgets()
  
    def create_widgets(self):
        """ create buttone which displays num of clicks"""
        self.button1 = Button(self)
        self.button["text"] = " total clicks: 0"
        self.button["command"] = self.update_count
        self.button1.grid()
  
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "Button2")
   
    def update_count(self):
        """ increase the count and display total"""
        self.button_clicks += 1
        self.button["text"] = "Total Clicks: " + str(self.button_clicks)
   
root = tkinter.Tk()
root.title("show buttons")
root.geometry("200x100")

app = Application(root)
root.mainloop()
