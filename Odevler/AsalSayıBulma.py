
def AsalSayı(x):
    if (x == 1 or x <=1):
        return("Yanlış Sayı Girdiniz")
    elif (x == 2):
        return("2 Asal Sayıdır")
    else:
        toplam = 2
        while True:
            if x%toplam == 0:
                return("{} Asal Sayı değildir".format(x))
            else:
                toplam = toplam +1
                if toplam == x :
                    break
                else:
                    pass
            break
AsalSayı(10)
        
            

        
            



























