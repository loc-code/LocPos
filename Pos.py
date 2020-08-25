from tkinter import *
import sys
from tkinter import messagebox
def Login():
	if entry_username.get() == "phuc.ntsc@gmail.com" and entry_password.get() == "GaoShanCHa@2018":
		messagebox.showinfo("Welcome", "Welcom Huỳnh Thị Ngọc Thạnh")
		root.deiconify()
		top.destroy()
	elif entry_username.get() == "admin" and entry_password.get() == "":
		messagebox.showinfo("Welcome", "Welcom Nguyễn Tiến Lộc")
		root.deiconify()
		top.destroy()

	# For False Password and Username
	elif entry_username.get() == "" and entry_password.get() == "":
		messagebox.showinfo("Error", "Please fill in the blank")
	elif entry_username.get() != "phuc.ntsc@gmail.com" and entry_password.get() != "GaoShanCHa@2018" or entry_username.get() != "admin" and entry_password.get() != "":
		messagebox.showinfo("Error", "No Account")
		passw.set("")

def Cancel():
	top.destroy()
	root.destroy()
	sys.exit()

root = Tk()
top = Toplevel()

mainfont = ("Arial 25 bold")
passw = StringVar()

#Def Var
var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

# Set up Main Screen
top.geometry("300x260")
top.title("Login System")
top.configure(bg = "Cadet Blue")
top.attributes('-fullscreen', True)
lbl_username = Label(top, text = "Username:", bg = "Cadet Blue", font = mainfont)
entry_username = Entry(top, font = mainfont)
lbl_password = Label(top, text = "Password:", bg = "Cadet Blue", font = mainfont)
entry_password = Entry(top, textvariable = passw, font = mainfont, show = "*")
Cancel_btn = Button(top, text = "Cancel", font = mainfont, command = Cancel)
Login_btn = Button(top, text = "Login", font = mainfont, command = Login)
lienceseLabel = Label(top, text = "LocPos Made By Loc", font = mainfont, width = 100, bg = "Lime")

lbl_username.pack(side = TOP, pady = 2)
entry_username.pack(side = TOP,)
lbl_password.pack(side = TOP, pady = 5)
entry_password.pack(side = TOP)
Login_btn.pack(side = TOP, pady = 5)
Cancel_btn.pack(side = TOP, pady = 5)
lienceseLabel.pack(side = BOTTOM)
# Main
root.geometry("1350x750+0+0")
root.title("Milktea Management System")
root.attributes('-fullscreen', True)
root.configure(bg = "Cadet Blue")

Tops = Frame(root, bg = "Cadet Blue", bd = 20, pady = 5, relief = RIDGE)
Tops.pack(side = TOP)

lblTitle = Label(Tops, font = ("Arial 52 bold"), text = "Milktea Management System", bd = 21, bg = "Cadet Blue", fg = "Cornsilk", justify = CENTER)
lblTitle.grid(row = 0, column = 0)

Receptcal_F = Frame(root, bg = "Powder Blue", bd = 10, relief = RIDGE)
Receptcal_F.pack(side = RIGHT)
Buttons_F = Frame(Receptcal_F, bg = "Powder Blue", bd = 3, relief = RIDGE)
Buttons_F.pack(side = BOTTOM)
Cal_F = Frame(Receptcal_F, bg = "Powder Blue", bd = 6, relief = RIDGE)
Cal_F.pack(side = TOP)
Receipt_F = Frame(Receptcal_F, bg = "Powder Blue", bd = 4, relief = RIDGE)
Receipt_F.pack(side = BOTTOM)

MenuFrame = Frame(root, bg = "Cadet Blue", bd = 10, relief = RIDGE)
MenuFrame.pack(side = LEFT)
CostFrame = Frame(MenuFrame, bg = "Powder BLue", bd = 4)
CostFrame.pack(side = BOTTOM)
DrinksFrame = Frame(MenuFrame, bg = "Cadet Blue", bd = 10)
DrinksFrame.pack(side = TOP)

DrinksFrame = Frame(MenuFrame, bg = "Cadet Blue", bd = 10, relief = RIDGE)
DrinksFrame.pack(side = LEFT)
ToppingFrame = Frame(MenuFrame, bg = "Powder Blue", bd = 10, relief = RIDGE)
ToppingFrame.pack(side = RIGHT)

truyenThongM = Checkbutton(DrinksFrame, text = "Truyền Thống M", variable = var, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 0, sticky = W)
truyenThongL = Checkbutton(DrinksFrame, text = "Truyền Thống L", variable = var1, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 1, sticky = W)
ThaiXanhM = Checkbutton(DrinksFrame, text = "Thái Xanh M", variable = var4, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 2, sticky = W)
ThaiXanhL = Checkbutton(DrinksFrame, text = "Thái Xanh L", variable = var5, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 3, sticky = W)
truyenThongThapCamM = Checkbutton(DrinksFrame, text = "Truyền Thống Thập Cẩm M", variable = var2, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 4, sticky = W)
truyenThongThapCamL = Checkbutton(DrinksFrame, text = "Truyền Thống Thập Cẩm L", variable = var3, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 5, sticky = W)
truyenThongM = Checkbutton(DrinksFrame, text = "Thái Xanh Thập Cẩm M", variable = var6, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 6, sticky = W)
truyenThongM = Checkbutton(DrinksFrame, text = "Thái Xanh Thập Cẩm L", variable = var7, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 7, sticky = W)
truyenThongM = Checkbutton(DrinksFrame, text = "Truyền Thống M", variable = var8, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 8, sticky = W)
truyenThongM = Checkbutton(DrinksFrame, text = "Truyền Thống M", variable = var9, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 9, sticky = W)
truyenThongM = Checkbutton(DrinksFrame, text = "Truyền Thống M", variable = var10, onvalue = 1, offvalue = 0, font = ("Arial 18 bold"), bg = "Cadet Blue").grid(row = 10, sticky = W)




















root.withdraw()
root.mainloop()
