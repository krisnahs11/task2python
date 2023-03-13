import tkinter   as tk

root = tk.Tk()
root.geometry('500x300+500+300' )

menubar =tk.Menu(root)

file =  tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file)

file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Close")

file.add_separator()
file.add_command(label="Exit", command=root.quit)

edit= tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="edit", menu=edit)
edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_command(label="Paste")

root.config(menu=menubar)
root.mainloop()
