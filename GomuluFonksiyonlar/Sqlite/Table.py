#Sqlite İlişkisel Veri Tabanı
import sqlite3

# con = sqlite3.connect("kütüphane.db")
# cursor = con.cursor()

# def newTable():
#     cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim TEXT,yazar TEXT,Yayınevi TEXT,Sayfa_Sayisi INT)")
#     con.commit()

# newTable()
# con.close()

#Tablolara Veri Ekleme

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def newTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim TEXT,yazar TEXT,Yayınevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veriekle():
    cursor.execute("INSERT INTO kitaplik VALUES('İstanbul Hatırası','Ahmet Ümit','Everest','66')")
    con.commit()
def veriekle2(a,b,c,d):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(a,b,c,d))
    con.commit()
def VerileriAL():
    cursor.execute("Select * from kitaplik")
    liste = cursor.fetchall()
    print(liste)
def verilerial2():
    cursor.execute("Select isim,yazar from kitaplik")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def verilerial3(yayınevi):
    cursor.execute("Select * from kitaplik where yayinevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def verileriguncelle(a,b):
    cursor.execute()
    cursor.execute("Update kitaplik set yayınevi = ? where yayınevi = ?",(a,b))
    con.commit()
def verilerisilme(a):
    cursor.execute("Delete From kitaplik where yazar = ?"(a,))
    con.commit()

# isim =input("İsim:")
# yazar =input("Yazar:")
yayinevi =input("Yanınevi:")
# sayfasayisi =int(input("Sayfa Sayısı:"))
newTable()
verilerial2()
verilerial3(yayinevi)
veriekle()
VerileriAL()
# veriekle2(isim,yazar,yayinevi,sayfasayisi)
con.close()
#Tablodan Verileri Çekme




