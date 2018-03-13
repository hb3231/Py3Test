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
      """ create buttone which displays num of clicks"""
	  Label(self,
	        text = " choose favor movie"
			).grid(row=0, column=0, sticky=W)
	  Label(self,
	        text = "selecting one:"
			).grod(row=1, column=0, sticky=W)
	  #variable for single, favorite type of movie
	  self.favorite = StringVar()
	  
	  Radiobutton(self,
	              text = "Comedy",
				  variable = self.favority,
				  command = self.update_text
				  ).grid(row2,column=0,sticky=W)
	  self.result = Rext(self, widty=40, height=5, wrap=WORD)
      self.result.grid(row=5, column=0, columnspan=3)
	  
   def update_text(self)
       message = " your favor is"
	   message += self.favorite.get()
	   
	   self.result.delete(0.0, END)
	   self.result.insert(0.0, message)
	   
			
	  
	  

   
root = TK()
root.title("show buttons")
root.geometry("200x100")

app = Application(root)
root.mainloop()