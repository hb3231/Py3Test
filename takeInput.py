#Simple GUI
from Tkinter import *
class Application(Frame):
   """ A GUI application  """
   def _init_(self, master):
      """ init the frame"""
	  Frame._init_(self,master)
	  self.grid()
	  self.create_widgets()
	  
   def create_widgets(self):
      """ create buttone , text, entry widgets"""
	  self.insuruction = Label(self, text = "Entre the passord")
	  self.instruction.grid(row = 0, column =0, columnspan =2, sticky = W)   # put label left side
	  
	  self.password = Entry(self)
	  self.password.grid(row = 1, column =1, sticky = W)
	  
	  self.submit_button = Button(self, text = " Submit", command = self.reveal)
	  self.submit_button.grid(row = 2, column=0, sticky = W)
	  
	  self.text = Text(sel, widty = 35, height=5, wray = WORD)
	  selftext.grid(row =3, column=0, columnspan =2, sticky = W)
	  
   def reveal(self):
      """ display msg """
	  content = self.passwork.get()
	  
	  if content == " password":
	     message = " you have access to smth"
	  else:
	     message = " Access denied"
		 
	  self.text.inert(0.0, message)
	  
   
root = TK()
root.title("Passwork")
root.geometry("200x100")

app = Application(root)
root.mainloop()