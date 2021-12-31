print("""1.Bakiye Sorgulama
2.Para yatırma
3.Para Çekme
Programndan Çıkmak için 15'e basınız.""")

bakiye = 1000 

while True:

    giris = int(input("Lütfen işlemi seçiniz"))

    if giris == 1 :
        print("Şuanda Bakiyeniz {} TL'dir".format(bakiye))
    elif giris == 2 :
        para = int(input("Yatırmak istediğiniz para miktarını yazınız."))
        bakiye = bakiye+para
        print("Paranız yatırıldı. Güncel bakiyeniz {} TL'dir".format(bakiye))
    elif giris == 3 : 
        para = int(input("Çekmek istediğiniz para miktarını yazınız."))
        if para > bakiye:
            print("Bakiye miktarından daha fazla çekemezsiniz")
        else:
            bakiye = bakiye-para
            print("Para çekimi başarılı.Güncel Bakiyeniz {} TL'dir".format(bakiye))
    elif giris == 15 :
        print("Çıkış Yapıldı")
        break
    else:
        print("Yanlış Girişi Yaptınız Lütfen Doğru seçim Yapınız")        
























