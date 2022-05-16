from tkinter import *
from tkinter import ttk

# The root or main window holding all widgets 
root = Tk()
root.title("Basic GUI App")

# individual widgets need to be connect to the root
# and their own characteristics specified
label_1 = Label(root, text="This is a label")
label_2 = Label(root, text="A second label")

# quick push to root window
# builtin algo for placement
label_1.pack()
label_2.pack()

# place using x and y pixel positions
# label_1.place(x=100, y=100)
# label_2.place(x=50, y=100)

# place relative to parent using 0.0-1.0 as percent
# label_1.place(relx=0.5)
# label_2.place(relx = 0.5, rely=0.5)

# adjust dimension of widget withoffset
# label_1.place(height=100, width=100)
# label_2.place(height=100, width=100, x=100)

# create loop 
root.mainloop()
