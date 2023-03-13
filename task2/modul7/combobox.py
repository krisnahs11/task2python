import tkinter as tk

from tkinter import ttk

from functools import partial

def fungsitampil(labelhasil, namacbBox):
    nl=namacbBox.get()
    hasil=nl
    labelhasil.config(text=hasil)
    return

root= tk.Tk()
root.title('ComboBox')
root.geometry("500x300+600+200")

root.option_add('*font', ('Verdana', 10, 'normal'))
root.option_add('*label.font', ('Verdana',10, 'normal'))
labelpilihoperator=tk.Label(root, text="Pilih Operator")
labelpilihoperator.grid(row=0, column=0, sticky="W", padx=(5,0),pady=(5,5))

namacbBox= tk.StringVar()
combopilihoperator=ttk.Combobox(root, values=["+","-","*","/"], textvariable=namacbBox)
combopilihoperator.grid(row=1, column=0, padx=(5,0), pady=(0,5))

combopilihoperator.current(0)

labelhasil= tk.Label(root)
labelhasil.grid(row=3, column=0)

tampil = partial( fungsitampil, labelhasil, namacbBox)
tomboltampil= tk.Button(root, text="tampil", command=tampil)
tomboltampil.grid(row=2, column=0, sticky="WE", padx=(5,0))
tomboltampil.configure(bg="#000", fg="#FFF")

root.mainloop()