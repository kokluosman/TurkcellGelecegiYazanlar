#Kümeler
from typing import Union


x ={1,2,3}
# Her elemandan 1 tane olur
# Sırasızdır.Indexlerle ulaşılmaz.Indexsizdir
x = {"Elma","Armut","Kiraz","Muz"}

for i in x:
    print(i)

#Küme Metodları

#add() içindeki elemanı ekler. Eğer varsa eklemez

#difference() farkı söyler
küme1 = {1,2,3,4,5,6,-2,9}
küme2 = {1,2,23,34,-1}
liste = küme1.difference(küme2)
print(liste)

#x.discard(a) a elamanını x kümesinden çıkarır

#a.Intersection(b) a ile b kümesi elemanlarının kesişimi

#x.isdisjoint(y) x ile y kesişimi boş ise true,değilse False döner

#x.issubset(y) x y'nin alt kümesi mi diye sorar. Alt kümeyse True değilse False döner

#x.union(y) x ile y kümesinin birleşimini söyler.







