#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os


class Database():
    def __init__(self, filename="address_book.db"):
        self.dbfilename = filename
        if os.path.exists(self.dbfilename):
            #print("Dosya mevcut olduğu için yeni dosya oluşturulmadı!")
            pass
        else:
            print("Database dosyası oluşturuldu!")
            db = sqlite3.connect(self.dbfilename)
            db.execute('PRAGMA encoding="UTF-8"')
            c = db.cursor()
            c.execute(
                "CREATE TABLE IF NOT EXISTS records\
                (record_id INTEGER PRIMARY KEY, \
                name TEXT, \
                last_name TEXT, \
                phone_number TEXT, \
                email_address TEXT \
                )")
            db.commit()
            c.close()

    def truncate(self):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.executescript("DELETE FROM records; VACUUM;")
        db.commit()
        c.close()

    def add_record(self, name='', last_name='', phone_number='', email_address=''):
        db = sqlite3.connect(self.dbfilename)
        # db.text_factory = lambda x: unicode(x, 'utf-8', 'ignore') #It converts strings into unicode objects.
        # name=name.decode('utf8')
        # last_name=last_name.decode('utf8')

        c = db.cursor()
        c.execute("INSERT INTO records(name, last_name, phone_number, email_address) VALUES (?,?,?,?)",
                  (name, last_name, phone_number, email_address))
        db.commit()
        c.close()

    def update_record(self, id, name, last_name, phone_number, email_address):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute("UPDATE records SET name=?, last_name=?, phone_number=?, email_address=? WHERE record_id=?",
                  (name, last_name, phone_number, email_address, id))
        db.commit()
        c.close()

    def delete_record(self, record_id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('DELETE FROM records WHERE record_id = ?', (record_id,))
        db.commit()
        c.close()

    def list_all(self, ):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute('SELECT * FROM records')
        records = c.fetchall()
        c.close()
        return records

    def fromid(self, id):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute("SELECT * FROM records WHERE record_id=?", (id,))
        records = c.fetchall()
        c.close()
        return records

    def fromname(self, ad):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute("SELECT * FROM records WHERE name LIKE ? OR last_name LIKE ?", ("%" + ad + "%", "%" + ad + "%"))
        records = c.fetchall()
        c.close()
        return records

    def fromphone(self, phone):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute("SELECT * FROM records WHERE phone_number LIKE ?", ("%" + phone + "%",))
        records = c.fetchall()
        c.close()
        return records

    def fromemail(self, email):
        db = sqlite3.connect(self.dbfilename)
        c = db.cursor()
        c.execute("SELECT * FROM records WHERE email_address LIKE ?", ("%" + email + "%",))
        records = c.fetchall()
        c.close()
        return records
