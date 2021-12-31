#Decorator
import time
def kare(sayılar):
    sonuç = list()
    baslama = time.time()
    for i in sayılar:
        sonuç.append(pow(i,2))
    bitis = time.time()
    print("Bu fonksiyon "+str(bitis-baslama)+"sn sürdü")
def küp(sayilar):
    sonuç = list()
    baslama = time.time()

    for i in sayilar:
        sonuç.append(pow(i,2))
    bitis = time.time()
    print("Bu fonksiyon "+str(bitis-baslama)+"sn sürdü")

#Veya aşağıdaki gibi decorator ile

def zaman(func):
    def wrapper(sayilar):
        baslama = time.time()

        sonuç = func(sayilar)

        bitis = time.time()

        print(func.__name__+ ' ' + str(bitis-baslama) + 'saniye surdu.' )
        return sonuç
    return wrapper
@zaman
def kare(sayılar):
    sonuç = list()
    for i in sayılar:
        sonuç.append(pow(i,2))
@zaman
def küp(sayilar):
    sonuç = list()

    for i in sayilar:
        sonuç.append(pow(i,2))
    
    

kare(range(100000))































