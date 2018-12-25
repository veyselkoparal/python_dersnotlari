#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *


class frm_new:
    def __init__(self, parent, record=''):
        if record != '':
            self.updateid = record[0][0]
            ad = record[0][1]
            soyad = record[0][2]
            telefon = record[0][3]
            email = record[0][4]
        else:
            self.updateid = -1
            ad = ''
            soyad = ''
            telefon = ''
            email = ''

        self.pencere = Toplevel()
        self.pencere.title("Rehbere Yeni Kişi Ekle")

        self.ust = Label(self.pencere)
        self.ust.config(text="Henüz ekleme yapılmadı.")
        self.ust.pack()

        self.iste = Label(self.pencere)
        self.iste.config(text="Lütfen İsmi Giriniz:")
        self.iste.pack()

        self.isim = Entry(self.pencere)
        self.isim.insert(0, ad)
        self.isim.focus_set()
        self.isim.pack()

        self.iste2 = Label(self.pencere)
        self.iste2.config(text="Lütfen Soyisim Giriniz:")
        self.iste2.pack()

        self.soyad = Entry(self.pencere)
        self.soyad.insert(0, soyad)
        self.soyad.pack()

        self.iste3 = Label(self.pencere)
        self.iste3.config(text="Lütfen Telefon Numarasını Giriniz:")
        self.iste3.pack()

        self.telefon = Entry(self.pencere)
        self.telefon.insert(0, telefon)
        self.telefon.pack()

        self.iste4 = Label(self.pencere)
        self.iste4.config(text="Lütfen E-Mail Adresini Giriniz:")
        self.iste4.pack()

        self.email = Entry(self.pencere)
        self.email.insert(0, email)
        self.email.pack()

        self.ekleme = Button(self.pencere, text="Kaydet!", command=lambda: self.kaydet())
        self.ekleme.pack()

        parent.wait_window(self.pencere)

    def kaydet(self):
        ad = self.isim.get()
        soyad = self.soyad.get()
        telefon = self.telefon.get()
        email = self.email.get()

        import Database
        if self.updateid > 0:
            islem = Database.Database().update_record(self.updateid, ad, soyad, telefon, email)
        else:
            islem = Database.Database().add_record(ad, soyad, telefon, email)
        self.ust.config(text="Son Eklenen: %s %s" % (ad, soyad))
        self.pencere.destroy()
