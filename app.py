from tkinter import * 
import tkinter
from typing import List

window = tkinter.Tk()
window.title("TV Shows Tracker")

# Change background of the canvas
# window.configure(background='#FFF4C8')

# Input 
name = Label(window, text="Name")
name.grid(column=0, row=0)

note = Label(window, text="Note")
note.grid(column=0, row=1)

name_entry = Entry(window, takefocus=True)
name_entry.grid(column=1, row=0)
# name_entry.grid(column=1, row=0, columnspan=3)

note_entry = Entry(window)
note_entry.grid(column=1, row=1)
# note_entry.grid(column=1, row=1, columnspan=2)

# Buttons 
add = Button(window, text='Add')
add.grid(column=0, row=2)

edit = Button(window, text='Edit')
edit.grid(column=1, row=2)

view_all = Button(window, text='View all')
view_all.grid(column=2, row=2)

delete = Button(window, text='Delete')
delete.grid(column=0, row=3)

search = Button(window, text='Search')
search.grid(column=1, row=3)

# Listbox
listbox = Listbox(window, height=6, width=35)
listbox.grid(column= 0, row=4, columnspan=2, rowspan=6)

window.mainloop()