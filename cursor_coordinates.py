from tkinter import *
import pyautogui as pg

buttonyes = True


def cursor():
	coordinates = pg.position()
	label2 = Label(root, text = coordinates,font=('Arial Bold',30))
	label2.place(x = 220, y = 350, height = 50, width = 165)
	label2.after(60, cursor)
	buttonyes = False
	BigX = False
	BigY = False
	if buttonyes == False:
		button1.destroy()
		labelx = Label(root, text = 'X', font=('Arial Bold',20)) 
		labelx.place(x = 220, y = 290)
		labely = Label(root, text = 'Y', font=('Arial Bold',20))
		labely.place(x = 360 , y = 290)

root = Tk()
root.title('Coordinates')
root.geometry('600x600')
canvas = Canvas(root, width=1000, height=1000, bg= '#00FA9A')

canvas.pack()


label1 = Label(root, text = 'Cursor coordinates ', font=('Arial Bold',30))
label1.place(x = 130, y = 100)
button1 = Button(root, text = 'Launch ', command = cursor )
button1.place(x = 270, y = 200)

root.mainloop()

# Copyright (c) 2020 Unbewohnte

