'''
Proof of concept for an binary calculator app in order
to further get used to using tKinter and python.

http://tkdocs.com/index.html

Notes:
0b1 = "1"
0b0 = "0"
-0b1 = "-1"
'''
from tkinter import *
from tkinter import ttk
import tkinter as tk

# global variables
operator = ""
stored_num = "0b0"

# The root or main window holding all widgets 
root = Tk()
root.title("Binary Calculator")
root.geometry("300x300+900+100")

# variable text for lable_0 decimal representation of label_0
dec_str = tk.StringVar()
dec_str.set("")

# variable text for label_1 
label_str = tk.StringVar()
label_str.set("")

# set weights for grid. can be done individuall
# but for equal weights it can be done in loops
root.grid_rowconfigure(0, weight=1)
for row in range(1, 4):
	root.grid_rowconfigure(row, weight=2)

for col in range(3):
	root.grid_columnconfigure(col, weight = 2)

def bin_to_dec(num_str):
	"""convert a binary string to decimal
    
    Args:
        num_str (string): a binary string w/ or w/o b form
 
    Returns:
        string: the decimal value of num_str
    """
	dec_value = num_str
	if 'b' in num_str:
		dec_value = bin_display(num_str)
		

	return int(dec_value, 2)

def bin_display(num_str):
	"""remove begining of binary string to remove
	0b and - symbol
    
    Args:
        num_str (string): a binary string in 0b form
 
    Returns:
        string: binary string wthout b
    """
	display_as = ""
	if '-' in num_str:
		display_as = num_str[3:]
		if "-0" == display_as:
			display_as = "0"
	else:
		display_as = num_str[2:]
	return display_as

def clear():
	"""clear the calculator values and reset. Update display.

	Args:
        None
 
    Returns:
        None
    """
	global stored_num
	stored_num = "0b0"
	label_str.set("0")
	entry_field.delete(0, END)
	dec_str.set("")

	

def update_input(num):
	"""update binary number in entry field by appending num.
	Update display output. 
    
    Args:
        num (int): either 0 or 1 to append to entry field 
 
    Returns:
        None
    """

	# get what is in the entry field **str
	entry_value = entry_field.get() 
	
	# clear entry field
	entry_field.delete(0, END)

	# concatenate numbers with input num at the end **str
	new_number = entry_value + str(num)

	# push new number to display
	entry_field.insert(0, new_number)

	dec_str.set(bin_to_dec(new_number))
	
def sub():
	"""prepare calculator for performing subtraction between
	current number in entry and next number entered prior to 
	pressing equals. Update display outputs.
    
    Args:
        None
 
    Returns:
        None
    """
	global operator
	operator = "SUBTRACTION"
	# get value from entry field
	# if empty do nothing
	entry_value = entry_field.get() 
	if not entry_value:
		return
	
	# clear entry field to await no value
	entry_field.delete(0, END)

	# store the value from entry field into stored_num for future use **bin str
	global stored_num
	# stored_num = bin(int(entry_value, 2))
	stored_num = bin(int(stored_num, 2) - int(entry_value, 2))

	# display stored num in label
	label_str.set(bin_display(stored_num))	

def add():
	"""prepare calculator for performing addition between
	current number in entry and next number entered prior to 
	pressing equals. Update display outputs.
    
    Args:
        None
 
    Returns:
        None
    """
	global operator
	operator = "ADDITION"
	# get value from entry field
	# if empty do nothing
	entry_value = entry_field.get() 
	if not entry_value:
		return
	
	# clear entry field to await no value
	entry_field.delete(0, END)

	# store the value from entry field into stored_num for future use **bin str
	global stored_num
	# stored_num = bin(int(entry_value, 2))
	stored_num = bin(int(stored_num, 2) + int(entry_value, 2))

	# display stored num in label
	label_str.set(bin_display(stored_num))
		
def equal():
	"""perform addition or subtraction between number in 
	store_num and current number in entry field. Update
	display output.
    
    Args:
        None
 
    Returns:
        None
    """
	global operator
	global stored_num

	# get value from entry field
	# if empty do nothing
	entry_value = entry_field.get() 
	if not entry_value:
		return
	
	# clear entry field to await no value
	entry_field.delete(0, END)

	# perform calculation and update stored num **bin str
	if operator == "SUBTRACTION":
		stored_num = bin(int(stored_num, 2) - int(entry_value, 2))
	if operator == "ADDITION":
		stored_num = bin(int(stored_num, 2) + int(entry_value, 2))

	label_str.set(bin_display(stored_num))
	dec_str.set(bin_to_dec(stored_num))


# create the necessary widgets for the app
label_0 = Label(root, textvariable=dec_str,)
label_1 = Label(root, textvariable=label_str, justify=RIGHT)
entry_field = Entry(root, text="Enter number", relief="sunken", justify=CENTER)

button_0 = Button(root, text='0', command=lambda: update_input(0))
button_1 = Button(root, text='1', command=lambda: update_input(1))
button_clear = Button(root, text='C', bg="pink", command=clear)

button_minus = Button(root, text='-', command=sub)
button_plus = Button(root, text='+', command=add)
button_equal = Button(root, text='=', command=equal)

clear()

# display the widgets as desired using grid system
label_0.grid(row=0, column=0, sticky="W")
label_1.grid(row=0, column=1, columnspan=2, sticky="E")
entry_field.grid(row=1, column=0, columnspan=3,  sticky="NESW")

button_0.grid(row=2, column=0, sticky="NESW")
button_1.grid(row=2, column=1, sticky="NESW")
button_clear.grid(row=2, column=2, sticky="NESW")

button_minus.grid(row=3, column=0, sticky="NESW")
button_plus.grid(row=3, column=1, sticky="NESW")
button_equal.grid(row=3, column=2, sticky="NESW")

# create loop 
root.mainloop()
