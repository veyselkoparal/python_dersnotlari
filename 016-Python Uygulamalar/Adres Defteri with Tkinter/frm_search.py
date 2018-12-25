#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import Database


class frm_serach:
    db=Database.Database()
    def __init__(self,parent):

        self.pencere = Toplevel()
        self.pencere.title("Rehberde Arama Yap")
        self.pencere.geometry("300x250")

        ustcerceve = Frame(self.pencere)
        ustcerceve.pack()

        self.radyosecenegi = IntVar()
        Radiobutton(ustcerceve,
                    text="Id",
                    variable=self.radyosecenegi,
                    value=0).pack(anchor=W)
        Radiobutton(ustcerceve,
                    text="Ad-Soyad",
                    variable=self.radyosecenegi,
                    value=1).pack(anchor=W)
        Radiobutton(ustcerceve,
                    text="Telefon",
                    variable=self.radyosecenegi,
                    value=2).pack(anchor=W)
        Radiobutton(ustcerceve,
                    text="E-Mail",
                    variable=self.radyosecenegi,
                    value=3).pack(anchor=W)
        self.radyosecenegi.set(0)

        self.label = Label(self.pencere)
        self.label.config(text="Lütfen Aramak İstediğiniz Kelimeyi Girin:")
        self.label.pack(fill=X)

        self.entry = Entry(self.pencere)
        self.entry.focus_set()
        self.entry.pack()

        self.butisim = Button(self.pencere, text="İsimden Ara", fg="blue", command=self.ara).pack()

        self.message = Message(self.pencere)
        self.message.pack()

        parent.wait_window(self.pencere)

    def ara(self):
        text = self.entry.get()
        if self.radyosecenegi.get() == 0:
            gelen = self.db.fromid(text)
        elif self.radyosecenegi.get() == 1:
            gelen = self.db.fromname(text)
        elif self.radyosecenegi.get() == 2:
            gelen = self.db.fromphone(text)
        elif self.radyosecenegi.get() == 3:
            gelen = self.db.fromemail(text)

        if gelen == '':
            self.message.config("Kayıt Bulunamadı!")
        else:
            self.message.config(text=gelen)

        print("arama bitti")
