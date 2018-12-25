#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from Database import *


class rehber:
    db = Database()

    def __init__(self):
        self.anapencere = Tk()
        self.anapencere.title("Telefon Rehberim v1.0 ~ Veysel KOPARAL")
        self.anapencere.geometry("800x600")
        self.anapencere.resizable(width=FALSE,height=FALSE)

        x = (self.anapencere.winfo_screenwidth() - self.anapencere.winfo_reqwidth()) / 4
        y = (self.anapencere.winfo_screenheight() - self.anapencere.winfo_reqheight()) / 7
        self.anapencere.geometry("+%d+%d" % (x, y))

        self.kayitlar = Frame(self.anapencere)
        self.kayitlar.pack(fill=BOTH, expand=True)

        self.buttons = Frame(self.anapencere)
        self.buttons.pack(fill=BOTH, expand=True, side=LEFT)

        self.button = Button(self.buttons)
        self.button.config(text="Yeni Ekle", command=self.create_new)
        self.button.config(width=10, height=3, font=("Arial", 15, "bold"), bg="orange")
        self.button.pack(side=LEFT)

        self.button = Button(self.buttons)
        self.button.config(text="Sil", command=self.sil)
        self.button.config(width=10, height=3, font=("Arial", 15, "bold"), bg="red")
        self.button.pack(side=LEFT)

        self.button = Button(self.buttons)
        self.button.config(text="Tümünü Sil", command=lambda: self.sil(True))
        self.button.config(width=10, height=3, font=("Arial", 15, "bold"), bg="black", fg="white")
        self.button.pack(side=LEFT)

        self.button = Button(self.buttons)
        self.button.config(text="Düzelt", command=self.duzelt)
        self.button.config(width=15, height=3, font=("Arial", 15, "bold"), bg="green")
        self.button.pack(side=LEFT)

        self.button = Button(self.buttons)
        self.button.config(text="Rehberde Ara", command=self.create_search)
        self.button.config(width=15, height=3, font=("Arial", 15, "bold"), bg="brown")
        self.button.pack(side=RIGHT)

        self.tumunulistele()

        self.anapencere.deiconify()
        self.anapencere.mainloop()

    def create_new(self):
        import frm_new
        frm_new.frm_new(self.anapencere)
        self.tumunulistele()

    def create_search(self):
        import frm_search
        frm_search.frm_serach(self.anapencere)

    def sil(self, tumu=False):
        #import tkMessageBox
        from tkinter import messagebox as tkMessageBox
        if tumu:
            cevap = tkMessageBox.askyesno("UYARI", "Tüm Kayıtlar Silinsin mi?")
            if cevap == True:
                self.db.truncate()
                print("tum kayitlar silindi!")
        else:
            import frm_input
            id = frm_input.inputbox(self.anapencere, "Veri Girişi", "Silinecek Kayıt Id'si giriniz?", "1").value
            record = self.db.fromid(id)
            if record:
                cevap = tkMessageBox.askyesno("UYARI", "Kayıt Silinsin mi?")
                if cevap == True:
                    self.db.delete_record(int(id))
        self.tumunulistele()

    def duzelt(self):
        import frm_input
        id = frm_input.inputbox(self.anapencere, "Veri Girişi", "Düzeltilecek Kayıt Id'si giriniz?", "1").value
        print("gelen id:", id)

        record = self.db.fromid(int(id))
        if record:
            print(record)
            import frm_new
            frm_new.frm_new(self.anapencere, record)
        self.tumunulistele()

    def tumunulistele(self):
        kayitlar = self.db.list_all()
        print(kayitlar)

        self.totable(self.kayitlar, kayitlar)

    def totable(self, frame, data):
        # clear all child objects
        for widget in frame.winfo_children():
            widget.destroy()

        if len(data)>0:
            if len(data[0])>0:
                height = len(data)
                width = len(data[0])
                print("h =", height, "w =", width)
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        b = Entry(frame)
                        b.insert(0, data[i][j])
                        # b.configure(state='readonly')
                        b.grid(row=i, column=j)
