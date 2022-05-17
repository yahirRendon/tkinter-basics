'''
Example app of a binary calculator to further
get used to using tKinter
http://tkdocs.com/index.html
'''
from tkinter import *
from tkinter import ttk

def init_buttons():
	button_0 = Button(root, text='0')
	button_1 = Button(root, text='1')


# The root or main window holding all widgets 
root = Tk()
root.title("Binary Calculator")
# width x height position x + position y on screen
root.geometry("300x200+900+100")

# set weights for grid. can be done individuall
# but for equal weights it can be done in loops
for row in range(3):
	root.grid_rowconfigure(row, weight=1)

for col in range(3):
	root.grid_columnconfigure(col, weight = 1)

def clear():
	entry.delete(0, END)

def update_input(num):
	current_num  = entry.get()
	entry.delete(0, END)
	entry.insert(0, str(current_num) + str(num))

def addition():
	global first_num
	global operator
	operator = "ADDITION"
	current_num = entry.get()
	entry.delete(0, END)
	first_num = current_num

def subtraction():
	global first_num
	global operator
	operator = "SUBTRACTION"
	current_num = entry.get()
	entry.delete(0, END)
	first_num = current_num
	
def equal():
	current_num = str(entry.get())
	entry.delete(0, END)
	if operator == "ADDITION":
		answer = bin(int(first_num, 2) + int(current_num, 2))
	if operator == "SUBTRACTION":
		answer = bin(int(first_num, 2) - int(current_num, 2))

	entry.insert(0, answer[2:])

entry = Entry(root, text="Enter number", relief="sunken", justify="center")

button_0 = Button(root, text='0', command=lambda: update_input(0))
button_1 = Button(root, text='1', command=lambda: update_input(1))
button_clear = Button(root, text='C', bg="pink", command=clear)

button_minus = Button(root, text='-', command=subtraction)
button_plus = Button(root, text='+', command=addition)
button_equal = Button(root, text='=', command=equal)

entry.grid(row=0, column=0, columnspan=3,  sticky="NESW")

button_0.grid(row=1, column=0, sticky="NESW")
button_1.grid(row=1, column=1, sticky="NESW")
button_clear.grid(row=1, column=2, sticky="NESW")

button_minus.grid(row=2, column=0, sticky="NESW")
button_plus.grid(row=2, column=1, sticky="NESW")
button_equal.grid(row=2, column=2, sticky="NESW")

# create loop 
root.mainloop()
