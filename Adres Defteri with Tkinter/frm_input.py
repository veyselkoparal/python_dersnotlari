#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *


class inputbox:
    value=''
    def __init__(self, parent, title, message, default):
        self.pencere = Toplevel()
        self.pencere.title(title)
        self.pencere.geometry("300x75")

        self.label = Label(self.pencere)
        self.label.config(text=message)
        self.label.pack(fill=X)

        self.entry = Entry(self.pencere)
        self.entry.insert(0, default)
        self.entry.focus_set()
        self.entry.select_range(0,END)
        self.entry.pack(fill=X)

        self.button = Button(self.pencere)
        self.button.config(text="OK", width=10, command=self.ok)
        self.button.pack(pady=5)

        self.pencere.deiconify()
        self.pencere.wait_window()

    def ok(self):
        self.value=self.entry.get()
        self.pencere.destroy()
