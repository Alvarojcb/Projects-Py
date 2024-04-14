from tkinter import *
from tkinter import ttk

#colors
black = "#121010"
white = "#f5f2f2"
orange = "#db8604"
grey = "#ECEFF1"
blue = "#38576b"



window = Tk()
window.title('Calculadora')
window.geometry("400x525")
window.config(bg = black)

#frames
frame_screen = Frame(window, width= 400, height= 100, bg = blue)
frame_screen.grid(row = 0, column= 0)

frame_body = Frame(window, width= 400, height= 500, bg = white)
frame_body.grid(row = 1, column= 0)




#calculating
all_values = ''

def insert_values(event):
    global all_values
    all_values =  all_values + str(event)
    text_value.set(all_values)


def cal():
    global all_values
    result = eval(all_values)
    text_value.set(str(result))



def clean_screen():
    global all_values
    all_values = ""
    text_value.set("")



#creating label
text_value = StringVar()
app_label = Label(frame_screen, textvariable= text_value, width= 21, height= 4, padx=14, relief=FLAT, anchor = "e", justify=RIGHT,font="Ivy 22 bold", bg = blue, fg = white)
app_label.place(x= 0, y= 0)




#buttons
#first row
b1 = Button(frame_body, command= clean_screen,text="C", width= 20, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold", anchor= "center")
b1.place(x= 0,y= 0)

b2 = Button(frame_body,command=lambda: insert_values("%"),text="%", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b2.place(x= 200,y= 0)

b3 = Button(frame_body, command=lambda: insert_values("/"),text="/", width= 10, height= 4, bg=orange, fg=white, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b3.place(x= 300,y= 0)

#second row
b4 = Button(frame_body, command=lambda: insert_values("7"),text="7", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b4.place(x= 0,y= 85)

b5 = Button(frame_body, command=lambda: insert_values("8"),text="8", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b5.place(x= 100,y= 85)

b6 = Button(frame_body, command=lambda: insert_values("9"),text="9", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b6.place(x= 200,y= 85)

b7 = Button(frame_body, command=lambda: insert_values("*"),text="*", width= 10, height= 4, bg=orange, fg=white, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b7.place(x= 300,y= 85)


#thrid row
b8 = Button(frame_body, command=lambda: insert_values("4"),text="4", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b8.place(x= 0,y= 170)

b9 = Button(frame_body, command=lambda: insert_values("5"),text="5", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b9.place(x= 100,y= 170)

b10 = Button(frame_body, command=lambda: insert_values("6"),text="6", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b10.place(x= 200,y= 170)

b11 = Button(frame_body, command=lambda: insert_values("-"),text="-", width= 10, height= 4, bg=orange, fg= white ,relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b11.place(x= 300,y= 170)

#four row

b12 = Button(frame_body, command=lambda: insert_values("1"),text="1", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b12.place(x= 0,y= 255)

b13 = Button(frame_body, command=lambda: insert_values("2"),text="2", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b13.place(x= 100,y= 255)

b14 = Button(frame_body, command=lambda: insert_values("3"),text="3", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b14.place(x= 200,y= 255)

b15 = Button(frame_body, command=lambda: insert_values("+"),text="+", width= 10, height= 4, bg=orange, fg= white ,relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b15.place(x= 300,y= 255)

#fifth row

b16 = Button(frame_body, command=lambda: insert_values("0"),text="0", width= 20, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b16.place(x= 0,y= 340)

b17 = Button(frame_body, command=lambda: insert_values(","),text=".", width= 10, height= 4, bg=grey, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b17.place(x= 200,y= 340)

b18 = Button(frame_body, command= cal ,text="=", width= 10, height= 4, bg=orange, fg=white, relief=RAISED, overrelief= RIDGE,font="Ivy 13 bold")
b18.place(x= 300,y= 340)




window.mainloop()

