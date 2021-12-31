# #Dosya Açma ve Yazma İşlemleri

# # W dosya kipi
# # W kipi eğer oluşturmak istediğimiz dizinde yoksa yeni oluşturur. 
# # Eğer varsa onu silip yeni oluşturur. O yüzden biraz tehlikeli dosya erişme kipi

# # file = open("bilgiler.txt","w")

# # #Dosyaları mutlaka kapatmamız gerekiyor

# # file.close()
# # file = open("bilgiler.txt","w",encoding="utf-8")
# # file.write("Osman Köklü")
# # file.close()

# # A Dosya Kipi
# # eğer dosya yoksa oluşturur. Ama varsa açar

# file = open("bilgiler.txt","a",encoding="utf-8")

# file.write(" Osman köklü Naber Lan Manyak \n NE güzel Gülüyorsun buralardaaa")
# file.close()

# #Dosya Okuma İşlemleri

# # R kipi
# # Eğer dosya yoksa hata döndürür

# file = open("bilgiler.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")

# file.close()
# file = open("bilgiler.txt","r",encoding="utf-8")
# file.read()

# #Read ve ReadLine Fonksiyonları adı üzerinde


# #Readlines dosyaları liste tipinde döndürür
# dosya = open("bilgiler.txt","r",encoding="utf8")

# liste = dosya.readlines()
# print(liste)
# dosya.close()

# #Dosyalarda otomatik Kapatma

# with open("bilgiler.txt","r",encoding="utf-8") as file: # Bu otomatik kapatır. Dosya açıp kaparken bu mantıklı bayağa
#     print(file.tell()) # İmlecin nerede olduğunu söyler
#     file.seek(20)      # İmleci içine yazılan byte değerine götürür.
#     print(file.tell())

# Dosyalarda değişiklik yapmak

#r+ dosya kipi Hem dosyayı açar hemde yazma işlemi yaptırır.

# with open("bilgiler.txt","r+",encoding="utf-8") as dosya1:
#     dosya1.seek(10)
#     dosya1.write("Şuan Yazıyorum")


# Dostanın sonunda değişiklik yapmak
# A kipi dosya sonuna gidiyor

# with open("bilgiler.txt","a",encoding="utf-8") as dosyaa:
#     dosyaa.write("Merhaba Kardsim\n")
#     print(dosyaa)


# Dosyanın Başında Değişiklik Yapmak



# with open("bilgiler.txt","a",encoding="utf-8") as dosyaa:
#     icerik = dosyaa.read()
#     icerik = "laaa\n"+icerik
#     dosyaa.seek(0)

# Dosyanın ortasında değişiklik yapmak 

with open("bilgiler.txt","r+",encoding="utf-8") as dosyaa:
    liste = dosyaa.readlines()
    print(len(liste))
    liste.insert(2,"Yalan dünya")
    dosyaa.seek(0)
    for i in dosyaa:
        dosyaa.write(i)










