from tkinter import *
root= Tk()
root.title("Calculator")
#root.geometry("500*800")
ent=Entry(root, width=10,font=("arial", 50))
ent.grid( column=0,row=0, columnspan=10, padx=10, pady=10)

def add_key(number):
	NUM=str(ent.get())
	ent.delete(0, END)
	ent.insert(0, NUM+str(number))

def button_allclear():
	ent.delete(0, END)

def addi():
	num1= ent.get()
	global num_1
	global math
	math= "addition"
	num_1= int(num1)
	ent.delete(0, END)

def subs():
	num1= ent.get()
	global num_1
	global math
	math= "substraction"
	num_1= int(num1)
	ent.delete(0, END)
	
def multi():
	num1= ent.get()
	global num_1
	global math
	math= "multiplication"
	num_1= int(num1)
	ent.delete(0, END)
def divi():
	num1= ent.get()
	global num_1
	global math
	math= "division"
	num_1= int(num1)
	ent.delete(0, END)

def equal():
	num2= int(ent.get())
	ent.delete(0, END)
	
	if math=="addition":
		ent.insert(0, num_1 + num2)
	if math=="substraction":
		ent.insert(0, num_1 - num2)
	if math=="multiplication":
		ent.insert(0, num_1 * num2)
	if math=="division":
		ent.insert(0, num_1 / num2)	


#style= Style()
#style.configure('TButton',font=('Cambria',10),bg='#d1d3d4',fg='red')


first_button= Button(root, text='1', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(1))
second_button= Button(root, text='2', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda:add_key(2))
third_button= Button(root, text='3', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda:add_key(3))
four_button= Button(root, text='4', padx=35, pady=35, font='Cambria',bg='#E6F0FA',fg="red",command=lambda:add_key(4))
five_button= Button(root, text='5', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(5))
six_button= Button(root, text='6', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(6))
seven_button= Button(root, text='7', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(7))
eight_button= Button(root, text='8', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(8))
nine_button= Button(root, text='9', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(9))
zero_button= Button(root, text='0', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=lambda: add_key(0))

clear_button= Button(root, text='C',padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command= button_allclear)
equal_button= Button(root, text='=',padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command= equal)

add_button= Button(root, text='+', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=addi)
sub_button= Button(root, text='-', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=subs)
mul_button= Button(root, text='*', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=multi)
div_button= Button(root, text='/', padx=35, pady=35,font='Cambria',bg='#E6F0FA',fg="red",command=divi)

first_button.grid(row=3, column=0)
second_button.grid(row=3, column=1)
third_button.grid(row=3, column=2)

four_button.grid(row=2, column=0)
five_button.grid(row=2, column=1)
six_button.grid(row=2, column=2)

seven_button.grid(row=1, column=0)
eight_button.grid(row=1, column=1)
nine_button.grid(row=1, column=2)

zero_button.grid(row=4, column=0)
clear_button.grid(row=4, column=1)
equal_button.grid(row=4, column=2)

add_button.grid(row=1, column=3)
sub_button.grid(row=2, column=3)
div_button.grid(row=4, column=3)
mul_button.grid(row=3, column=3)

root.mainloop()