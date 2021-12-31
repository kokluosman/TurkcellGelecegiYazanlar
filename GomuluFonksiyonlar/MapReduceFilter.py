#Map() İlk Parametre fonkisyon, ikinci parametre liste,tuple vb.

def double(x):
    return x*2

print(list(map(double,[1,2,3,4,5,6,7])))

print(list(map(lambda x : x*2,[1,2,6,45])))

liste1 = [1,2,3,4]
liste2 = [4,5,6,7]
a=list(map(lambda x,y:x*y,liste1,liste2))
print(a)
#Reduce() İlk Parametre fonksiyon,ikinci parametre liste,tıple vb. Sıralı işlem Yapar Elemanlara

from functools import reduce
def toplama(x,y):
    return x+y

print(reduce(toplama,[12,18,20,30]))

print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))

#Filter() Reduce ile aynı. Tek farkı sorgu kısmında ifli ifade gibi matematiksel operatör var

print(list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8,9])))

def asal(x):
    i =2
    if x == i:
        return True
    elif x ==1 :
        return False
    else:
        while (i<x):
            if x % i ==0:
                return False
            i +=1
        return True 


a=list(filter(asal,range(0,101)))
print(a)

# Zip() iki liste tuple vb. elemanları birleştirir. ÜZerinde gezinmek içinde kullanılabilir.
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

for i,j in zip(liste1,liste2):
    print(i,j)

sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

a=list(zip(sözlük1.values(),sözlük2.values()))

print(a)
#Enumerate() Her Elemanı İndexleyerek Gruplandırır.

liste =["Elma","Armut","Muz","Kiraz"]

print(list(enumerate(liste)))

#All() Bütün değerler True ise True,en az bir değer False ise False Dönderir.
def herhangi(list):
    for i in list:
        if i:
            return True
        else:
            return False

print(all(liste))

#Any Bütün değerler False ise False, En az bir değer Tru ise True Dönderir.




