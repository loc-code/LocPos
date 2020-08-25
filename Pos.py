from tkinter import *
import sys
from tkinter import messagebox

def Login():
	if entry_username.get() == "phuc.ntsc@gmail.com" and entry_password.get() == "GaoShanCHa@2018" or entry_username.get() == "admin" and entry_password.get() == "":
		messagebox.showinfo("Welcome", "Huỳnh Thị Ngọc Thạnh")
		root.deiconify()
		top.destroy()
	else:
		messagebox.showinfo("Error", "No Account!")

def Cancel():
	top.destroy()
	root.destroy()
	sys.exit()

root = Tk()
top = Toplevel()

mainfont = ("Arial 13 bold")
passw = StringVar()

top.geometry("300x260")
top.title("Login System")
top.configure(bg = "Cadet Blue")
lbl_username = Label(top, text = "Username:", bg = "Cadet Blue", font = mainfont)
entry_username = Entry(top, font = mainfont)
lbl_password = Label(top, text = "Password:", bg = "Cadet Blue", font = mainfont)
entry_password = Entry(top, textvariable = passw, font = mainfont, show = "*")
Cancel_btn = Button(top, text = "Cancel", font = mainfont, command = Cancel)
Login_btn = Button(top, text = "Login", font = mainfont, command = Login)
lienceseLabel = Label(top, text = "LocPos", font = mainfont, width = 100, bg = "Lime")

lbl_username.pack(side = TOP)
entry_username.pack(side = TOP)
lbl_password.pack(side = TOP)
entry_password.pack(side = TOP)
Cancel_btn.pack(side = TOP)
Login_btn.pack(side = TOP)
lienceseLabel.pack(side = BOTTOM)

root.withdraw()
root.mainloop()
