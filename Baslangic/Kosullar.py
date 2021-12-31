#İf Else Elif

# islem = int(input("Sayı giriniz."))


# if islem == 1 :
    
#     print("Burası Dayı")


# elif islem == 2 :
    
#     islem = islem**2

#     print("Sayının karesi =",islem)

# else:
#     print("Yarrak")


a = input("Eğer Dörtgense Dörtgen yaz üçgense üçgen yaz")

if a =="Dortgen":
    x = input("ilk kenarı gir")
    b = input("ikinci kenarı gir")
    c = input("ücüncü kenarı gir")
    d = input("dorduncu kenarı gir")

    if x==b==c==d:
        print("Bu kare ede")
    else:
        print("Bu sıradan dikdorgen")


elif a =="Ucgen":
    x = input("ilk kenarı gir")
    b = input("ikinci kenarı gir")
    c = input("ücüncü kenarı gir")

    if x==b==c:
        print("Eşkenar üçgen")
    else:
        print("Eşkenar Üçgen Değil")



else:
    print("Yanlış girdin amınakoduğum")




















