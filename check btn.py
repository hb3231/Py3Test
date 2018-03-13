#Simple GUI
from Tkinter import *
class Application(Frame):
   """ A GUI application  """
   def _init_(self, master):
      """ init the frame"""
	  Frame._init_(self,master)
	  self.grid()
	  self.button_clicks = 0 #count the button clicks
	  self.create_widgets()
	  
   def create_widgets(self):
      """ create widgets for movie type choise"""
	  Lable(self, text = " choose a movie type").grid(row =0, column=0, sticky=W)
	  #instructions
	  Lable(self, text = "select all that apply:").grid(row=1, column=0, sticky = W)
	  #commedy check btn
	  self.comedy = BooleanVar()
	  Checkbutton(self, text="Comedy", variable = self.comedy, command = self.update_text).grid(row=2,column=0, sticky=W)
	  
	  self.result = Text(self, widty=40, height=5, wrap=WORD)
	  self.result.grid(row=5, column=0, columnspan=3)
   def update_text(self):
      likes = ""
	  if self.comedy.get():
	     likes +="uou like comedy."
		 

   
root = TK()
root.title("movies choise")
root.geometry("200x100")

app = Application(root)
root.mainloop()