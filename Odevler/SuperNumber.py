a = int(input("Bir Sayı Giriniz"))

toplam = 0

for i in range(1,a):
    if (a % i) ==0:
        toplam = toplam+i
    else:
        None

if a == toplam:
    print("{} Sayısı Mükemmel Sayıdır".format(a))
else:
    print("{} Sayısı Mükemmel Sayı Değildir".format(a))



























