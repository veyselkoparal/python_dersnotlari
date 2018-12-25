import sqlite3 as sql
import time
vt=sql.connect('program.sqlite')
imlec=vt.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS program(ders_adi,ders_gunu,ders_saati,ders_yeri)")
print("----------------- DERS PROGRAMIM -----------------")
def ders_ekle():
    ders_adi=input("Eklenecek dersin ismini veya kodunu giriniz.......:")
    ders_gunu=int(input("1-Pazartesi 2-Salı 3-Çarşamba 4-Perşembe 5-Cuma 6-Cuamrtesi 7-Pazar"))
    ders_saati=input("Ders saatinizi giriniz.......:")
    ders_yeri=input("Dersin yapılcağı dersliği giriniz....:")
    imlec.execute('INSERT INTO program (ders_adi,ders_gunu,ders_saati,ders_yeri) VALUES (?,?,?,?)',(ders_adi,ders_gunu,ders_saati,ders_yeri))
    vt.commit()


def ders_cikar():
    ders_adi=input("Çıkarılacak dersin ismini veya kodunu giriniz.......:")
    imlec.execute("Delete  From program where ders_adi= (?)",(ders_adi,))
    vt.commit()
    print("{} ders bilgisi siliniyor...".format(ders_adi))

def ders_guncellle():
    gun_secenek=int(input("Güncellencek Veri Çeşidi \n[1]Ders Adı [2]Ders Günü [3]Ders Saati [4]Ders Yeri"))
    if(gun_secenek==1):
        ders_adi=input("Güncellenecek dersin ismini veya kodunu giriniz.......:")
        ders_adig=input("Güncellenecek olan dersin yeni adını girin........:")
        imlec.execute('UPDATE program set ders_adi= ? WHERE ders_adi = ?',(ders_adig,ders_adi))
        print("{} İsimli ders {} ders olarak değiştirilmiştir.".format(ders_adi,ders_adig))
        vt.commit()

    elif(gun_secenek==2):
        ders_adi=input("Güncellenecek dersin ismini veya kodunu giriniz.......:")
        ders_gunug=input("Güncellenecek olan dersin yeni gününü girin........:")
        imlec.execute('UPDATE program set ders_gunu= ? WHERE ders_adi = ?',(ders_gunug,ders_adi))
        print("{} İsimli ders {} günü olarak değiştirilmiştir.".format(ders_adi,ders_gunug))
        vt.commit()
    elif(gun_secenek==3):
        ders_adi=input("Güncellenecek dersin ismini veya kodunu giriniz.......:")
        ders_saatig=input("Güncellenecek olan dersin yeni saatini girin........:")
        imlec.execute('UPDATE program set ders_saati= ? WHERE ders_adi = ?',(ders_saatig,ders_adi))
        print("{} İsimli ders saati {} olarak değiştirilmiştir.".format(ders_adi,ders_saatig))
        vt.commit()
    elif(gun_secenek==4):
        ders_adi=input("Güncellenecek dersin ismini veya kodunu giriniz.......:")
        ders_yerig=input("Güncellenecek olan dersin yeni yerini girin........:")
        imlec.execute('UPDATE program set ders_yeri= ? WHERE ders_adi = ?',(ders_yerig,ders_adi))
        print("{} İsimli dersin yeri {} olarak değiştirilmiştir.".format(ders_adi,ders_yerig))
        vt.commit()
    else:
        print("HATALI TUŞLAMA")
def goster():
    oku=imlec.execute('SELECT ders_adi,ders_gunu,ders_saati,ders_yeri from program')
    for verileri_cek in oku.fetchall():
        print('Ders İsmi: %s --- Ders Günü: %s --- Ders Saati: %s --- Derslik: %s '%verileri_cek)
    print("\n \n \n")
    vt.commit()

while True:
    secim=input("Programa Yapılcak İşlemi Seçiniz...\n[1] Ders Ekleme [2] Ders Güncelleme [3] Ders Çıkarma [4] Programımı Göster \n [Çıkmak için q tuşuna basınız]")
    if(secim=='q'):
        print("Sistemden çıkılıyor...")
        time.sleep(2)
        print("Sistemden başarıyla çıkış yapıldi")
        break
    elif(secim=='1'):
        ders_ekle()
        time.sleep(1)
        print("Girilen bilgiler Kayıt edilmiştir...")
    elif(secim=='2'):
        ders_guncellle()
        time.sleep(1)
        print("Girilen bilgiler Kayıt edilmiştir...")
    elif(secim=='3'):
        ders_cikar()
        time.sleep(1)
        print("Girilen bilgiler Kayıt edilmiştir...")
    elif(secim=='4'):
        goster()
    else:
        print("Hatalı işlem yaptınız....")
        vt.close()