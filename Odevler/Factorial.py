#Girilen sayının faktoriyelini hesaplayan program

sonuc = 1

while True:

    a = input("Lütfen Faktoriyelinin hesaplanmasını istediğiniz sayıyı giriniz")
    a = int(a)
    if False:
        None
    else:
        if a<0 : 
            print("Negatif Sayıların Faktoriyeli hesaplanamaz.")
            break
        elif a == 0:
            print("Cevap = 1")
            break
        else:
            for i in range(1,(a+1)):
                sonuc = sonuc*i
            print("{} Sayısının faktöriyeli = {}".format(a,sonuc))
            break
        













