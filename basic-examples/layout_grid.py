'''
Example of working with the grid system
http://tkdocs.com/index.html
'''
from tkinter import *
from tkinter import ttk

# The root or main window holding all widgets 
root = Tk()
root.title("Basic Grid App")
# width x height position x + position y on screen
root.geometry("300x300+900+100")

# set weights for grid. can be done individuall
# but for equal weights it can be done in loops
for row in range(3):
	root.grid_rowconfigure(row, weight=1)

for col in range(3):
	root.grid_columnconfigure(col, weight = 1)

# individual widgets need to be connected to the root
# and their own characteristics specified
label_1 = Label(root, background="bisque", text="1")
label_2 = Label(root, background="pink", text="2")
label_3 = Label(root, background="orange", text="3")

# display via desired grid settings
label_1.grid(row=0, column=0, sticky=(N, S, E, W))
label_2.grid(row=1, column=0, columnspan=2, sticky=(N, S, E, W))
label_3.grid(row=2, column=0, columnspan=3, sticky=(N, S, E, W))

# create loop 
root.mainloop()
