# Bir fonksiyon içinde başka fonksşyon tanımlamak

def fonksiyon():
    def fonksiyon2():
        print("Merhaba")

def toplam(*args):

    def toplam2(args):
        toplamlar = 0
        for i in args:
            toplamlar +=i
        return toplamlar
    print(toplam2(args))
toplam(1,2,3,4,5,6,7,8)

def anafonks(a):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam
    def çarpım(*args):
        çarpım = 1
        for i in args:
            çarpım = çarpım*i
        return çarpım
    if a == "toplama":
        return toplama
    else:
        return "çarpım"

fonk = anafonks("toplama")

print(fonk(1,2,4,5,6))

#Fonksiyonları ARgüman olarak başka fonksiyonşara gönderme

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def çarpma(a,b):
    return a*b
def bölme(a,b):
    return a/b

def anafonksiyon(func1,func2,func3,func4,islem_adi):
    
    if islem_adi == "toplama":
        print(func1(3,4))
    elif islem_adi == "cikarma":
        print(func2(10,3))
    elif islem_adi == "carpma":
        print(func3(3,5))
    else:
        print(func4(10,4))
anafonksiyon(toplama,cikarma,çarpma,bölme,"carpma")








