#Anahtar Değer ilişkilerine sahiptir.add()

sozluk = {"Ahmet":1,"Mehmet":2,"Osman":3,"NaletOlsun":4}

print(type(sozluk))

sozluk2 = dict()

print(sozluk2)

#Sozluk değerleri erişme Anahtar kelimeler yardımı ile erişilir.

print(sozluk["Ahmet"])


# Dinamik olarak eleman eklenebilir

sozluk["Yeni"] =5

print(sozluk)

a = {"bir" :[1,2,3,4],"iki":[[1,2],[3,4],[5,6]],"üç":15 } 

print(a["iki"][1][1])

#Sözlüklerin anahtar değeri değiştirme

a["üç"] = [[5,6,7],[2,3,4]]

print(a)

#İç içe sözlük oluşturulabilir.

#Sözlük metodlarını görelim

print(a.keys())
print(a.values())
print(a.items())#İçinde demet şeklinde yapıyor. O şekilde kullanabilirsin.












