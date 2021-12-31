a = input("Lütfen 4 basamaklı Bir Sayı Giriniz")
z = a
if len(a) == 4:
    a = int(a)
    b = z[0]
    c = z[1]
    d = z[2]
    e = z[3]
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    data = (b**4)+(d**4)+(c**4)+(e**4)
    if a == data:
        print("{} Sayısı Armstrong Sayıdır.".format(a))
    else:
        print("{} Sayı Armstrong sayı değildir".format(a))

else:
    print("Girilen Sayı 4 basamaklı Sayı değildir.")



















































