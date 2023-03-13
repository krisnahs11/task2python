import tkinter as tk
from functools import partial

def fungsitampil(labelhasil,rb):
    ambil= rb.get()
    hasil = ambil
    labelhasil.config(text=hasil)
    return

root= tk.Tk()
root.title('RadioButton')
root.geometry('600x300+600+300')
root.option_add('*font', ('Verdana', 10, 'normal'))
root.option_add('*Label.font', ('Verdana', 10 , 'bold'))

labelpilihanjurusan= tk.Label(root, text="Pilih Jurusan")
labelpilihanjurusan.grid(row=0, column=0, sticky="W", padx=(5,0), pady=(5,5))

rbvalues= tk.IntVar()

rbSI= tk.Radiobutton(root, text="Sistem Informasi", variable=rbvalues, value=1)
rbSI.grid(row=1, column=0, sticky="W")
rbIF= tk.Radiobutton( root, text="Informatika", variable=rbvalues, value=2)
rbIF.grid(row=2,column=0,sticky="W")
rbAK= tk.Radiobutton(root, text="Akuntasi Komputer", variable=rbvalues, value=3)
rbAK.grid(row=3, column=0, sticky="W")

labelhasil= tk.Label(root)
labelhasil.grid(row=5, column=0)

tampil= partial(fungsitampil, labelhasil, rbvalues)
tomboltampil= tk.Button(root, text="tampil", command=tampil)
tomboltampil.grid(row=4,column=0, sticky="WE", padx=(5,0))
tomboltampil.configure(bg="#000", fg="#FFF")

root.mainloop()