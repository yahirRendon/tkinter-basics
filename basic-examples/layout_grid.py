'''
Example of working with the grid system
http://tkdocs.com/index.html
'''
from tkinter import *
from tkinter import ttk

# The root or main window holding all widgets 
root = Tk()
root.title("Basic Grid App")
root.geometry("300x300")

# set weights for grid. can be done individuall
# but for equal weights can be done in loops
for row in range(3):
	root.grid_rowconfigure(row, weight=1)

for col in range(3):
	root.grid_columnconfigure(col, weight = 1)

# individual widgets need to be connect to the root
# and their own characteristics specified
frame_1 = Label(root, background="bisque", text="1")
frame_2 = Label(root, background="pink", text="2")
frame_3 = Label(root, background="orange", text="3")

# quick push to root window
frame_1.grid(row=0, column=0, sticky=(N, S, E, W))
frame_2.grid(row=1, column=0, columnspan=2, sticky=(N, S, E, W))
frame_3.grid(row=2, column=0, columnspan=3, sticky=(N, S, E, W))

# create loop 
root.mainloop()
