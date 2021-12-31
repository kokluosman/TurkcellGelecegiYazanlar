#EBOB - EKOK

liste = []
def Ebob(a,b):
    toplam = 2
    while True:
        if (a % toplam == 0 and  b % toplam == 0 ):
            liste.append(toplam)
        else:
            None
        toplam = toplam+1
        if (toplam >=a or toplam >=b ):
            return liste
        else:
            continue

liste1 =[]
def Ekok(a,b):
    toplam = 2
    while True:
        if (a % toplam == 0 or  b % toplam == 0 ):
            liste.append(toplam)
        else:
            None
        toplam = toplam+1
        if (toplam >a and toplam >b ):
            return liste
        else:
            continue    

data = Ekok(12,24)

print(data)




























