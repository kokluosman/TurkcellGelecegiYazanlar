#Args keyword

def fonk(*args):
    for i in args:
        print(i)

fonk([1,2,3])

def fonks(isim,*args):
    print("İsim:",isim)

    for i in args:
        print(i)

fonks("Osman")

#Kwargs Argümanları isim vererek gönderebilirim

def kwa(**kwargs):
    for i,j in kwargs.items():
        print("Argüman İsmi",i,"Argüman Değeri",j)
kwa(isim = "Osman", Soyisim = "Köklü",Numara = 11234)


def esnek(*args,**kwargs):
    for i in args:
        print(i)

    print("------------------")
    for i , j in kwargs.items():
        print(i,j)

esnek(1,2,3,4,5,6,isim = "Osman", Soyisim = "Köklü",Numara = 21505017)







