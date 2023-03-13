import tkinter as tk
from functools import partial

def pertambahan (labelhasil, bil1, bil2):
    b1 = int(bil1.get())
    b2 = int(bil2.get())
    hasil = b1 + b2
    # config digunakan untuk mengakses object atribut setelah 
    labelhasil.config(text=hasil)
    return

root = tk.Tk()
root. geometry('400x200+500+200')

root.option_add('*font',('Verdana', 10,'normal'))

root.title('Aritmatika')

labelbilangan1 = tk.Label(root, text="masukan bilangan 1")
labelbilangan1.grid(row=0, column=0, padx=(10,20))
labelbilangan2 = tk.Label (root, text="masukan bilangan 2")
labelbilangan2.grid(row=1, column=0, padx=(10,20))

bilangan1= tk.StringVar()
bilangan2= tk.StringVar()

inputbilangan1 = tk.Entry(root, textvariable=bilangan1)
inputbilangan1.grid(row=0, column=1)
inputbilangan2 = tk.Entry(root, textvariable=bilangan2)
inputbilangan2.grid(row=1, column=1)

labelhasil = tk.Label(root)
labelhasil.grid(row=2, column=1)

pertambahan= partial(pertambahan, labelhasil, bilangan1, bilangan2)
tomboltambah = tk.Button(root, text="tambah", command=pertambahan)

tomboltambah.grid(row=2, column=0, sticky="WE", padx=(10,20), pady=(5,0))
tomboltambah.configure(bg="#000", fg="#FFF")

root.mainloop()