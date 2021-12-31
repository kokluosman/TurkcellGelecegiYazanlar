import os
from datetime import datetime

#print(dir(os))

#Blunduğu Dizini Söyler
print(os.getcwd())
#Bulunduğu dizindeki Klasörleri Listeler
print(list(i for i in os.listdir( )))
#Klasör Oluşturma
"""os.mkdir("Deneme1")
#İçiçe Klasör Oluşturma
os.makedirs()
#Silme
os.rmdir("Deneme1")"""
#os.rename("kütüphane.db","osman.db")
# print(os.stat("osman.db"))

# Os.walk() Verilen dizin altında ki dosya ve klasörleri liste olarak döner
for i in os.walk("C:/Users/user/Desktop"):
    print(i)















