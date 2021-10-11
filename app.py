from tkinter import *
import tkinter 
import backend 


def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    name.delete(0, END)
    name.insert(END, selected_tuple[1])
    note.delete(0, END)
    note.insert(END, selected_tuple[2])


def add_func():
    backend.insert(name_text.get(), note_text.get())
    listbox.delete(0, END)
    listbox.insert((name_text.get(), note_text.get()))


def edit_func():
    backend.update(selected_tuple[0], name_text.get(), note_text.get(), selected_tuple[2])


def view_func():
    listbox.delete(0, END)
    for list in backend.view():
        listbox.insert(END, list[1:3])


def delete_func():
    backend.delete(selected_tuple[0])


def search_func():
    listbox.delete(0, END)
    for list in backend.search(name_text.get(), note_text.get() or name_text.get() or note_text.get()):
        listbox.insert(END, list[1:3])


window = tkinter.Tk()
window.title("TV Shows Tracker")

# Change background of the canvas
# window.configure(background='#FFF4C8')


# Input 
name = Label(window, text="Name")
name.grid(column=0, row=0)

note = Label(window, text="Note")
note.grid(column=0, row=1)

name_text = StringVar()
name_entry = Entry(window, takefocus=True)
name_entry.grid(column=1, row=0)
# name_entry.grid(column=1, row=0, columnspan=3)

note_text = StringVar()
note_entry = Entry(window)
note_entry.grid(column=1, row=1)
# note_entry.grid(column=1, row=1, columnspan=2)


# Buttons 
add = Button(window, text='Add', command=add_func)
add.grid(column=0, row=2)

edit = Button(window, text='Edit', command=edit_func)
edit.grid(column=1, row=2)

view_all = Button(window, text='View all', command=view_func)
view_all.grid(column=2, row=2)

delete = Button(window, text='Delete', command=delete_func)
delete.grid(column=0, row=3)

search = Button(window, text='Search', command=search_func)
search.grid(column=1, row=3)


# Listbox with scroll
listbox = Listbox(window, height=6, width=35)
listbox.grid(column= 0, row=4, columnspan=2, rowspan=6)

scroll = Scrollbar(window)
scroll.grid(column=2, row=4, rowspan=6)

listbox.configure(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()