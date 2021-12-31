
liste = list()

def Bolen(x):
    for i in range(1,x+1):
        if x % i == 0:
            liste.append(i)
        else:
            pass
Bolen(30)
print(liste)