

# def toplama(a,b):
#     return a+b
# a=toplama(5,4)
# print(a)

#Parametre türleri

# def selamla(isim="Ahmet"): # Eğer varsayılan olarak tanımlama yaparsam çalışır. Yoksa iine değer girmek gerekir
#     print("Selam {}".format(isim))

# print(selamla("Mehmet"))

"""
def naber(*a): # Tupple Şeklinde içinde bu şekilde tutar
    toplam = 0
    for i in a:
        toplam = toplam + i
    return toplam
az = naber(1,2,3,4,5,6,7,8,9,10)
print(az)

"""
# Global ve Yerel Değişkenler
# Local Değişkenler fonksiyonların ve sınıfların içindedir
c=10
def topla():
    c = 2
    print(c)
print(topla())
print(c)
# Eğer global dyi değiştirmek istiyosak

d = 4
def taopama():
    global d
    d = 5
    
#Lambda İfadesi

def ikiylecarp(x):
    return x*2
#Yukarıda ki demektir aşağıdaki

ikiylecarpp = lambda x : x*2

a=ikiylecarpp(10)
print(a)



















