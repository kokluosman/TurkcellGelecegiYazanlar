import random
import time

rasgeleSayi = random.randint(1,40)
tahmin_hakki = 7

while True:
    tahmin = int(input("Tahminin"))
    if (tahmin<rasgeleSayi):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)

        print("Sayıyı Artırınız")

        tahmin_hakki -= 1
    elif (tahmin>rasgeleSayi):
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)
        
        print("Sayıtı düşürünüz")
        tahmin_hakki -= 1
    else:
        print("Bilgiler Sorgulanıyor")
        time.sleep(1)

        print("Tebrikler Doğru Bildiniz")
        break
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitti. Sayı {} idi.".format(rasgeleSayi))
        break
