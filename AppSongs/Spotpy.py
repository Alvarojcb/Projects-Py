from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

#cores 
black = "#131414"  
white = "#e1ede4"  
green = "#1bc245"  
letter = "#403d3d"   
blue = "#0d62bd" 


window = Tk()
window.title = ("Spotphy")
window.geometry = ('352x255')
window.configure(background = black)
window.resizable(width= FALSE, height=FALSE)

#frames

left_frame = Frame(window, width= 150, height= 150, bg = black)
left_frame.grid(row= 0 ,column= 0, pady =1, padx =1, sticky = NSEW)


right_frame = Frame(window, width= 250, height= 150, bg = black)
right_frame.grid(row= 0 ,column= 1, pady =1, padx =0, sticky = NSEW)

bottom_frame = Frame(window, width= 404, height= 100, bg = black)
bottom_frame.grid(row= 1 ,column= 0, columnspan= 3,pady =1, padx =1, sticky = NSEW)


#left frame
path = "AppSongs/img/iconapp.png"

icon = Image.open(path)
icon = icon.resize((130, 130))
icon = ImageTk.PhotoImage(icon)

l_icon = Label(left_frame, height = 130, image=icon, compound= LEFT, padx= 10, anchor='nw', font=('ivy 16 bold'), bg = black, fg= black)
l_icon.place(x = 24, y = 15)


#right frame



window.mainloop()