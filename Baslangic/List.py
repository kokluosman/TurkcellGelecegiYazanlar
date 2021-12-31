#Listeler

liste = ["ELma",34,"Osman",3.14,5]

print(type(liste))

a=list()
listeler=[]
print(len(liste)) # 5 Elemanlı olduğu için 5 dir.

liss=list("Merhaba")
print(liss)
#İndexleme ve parçalama işlemleri

print(liste[0:2]) # 0'dan başla 2ye kadar al ama 2yi alma

#İndexleme ve parçalama aynı string ifadelerdeki gibidir.

print(liste[::-1])

#listeler birbirleri ile toplanabilir veya string gibi çarpılabilir.

#Liste Metodları

#Append() ekleme metodu
liste.append("Ahmet")
print(liste)

#Pop metodu Son elemanı atar. İÇine değer verirsek index numarası olarak o indexi atar.
print(liste.pop())

#sort() metodu   İçindeki sayıları küçükten büyüğe sıralar.

data = [1,2,3,45,89,75,4,6,8,76,456,55]

b = data.sort(reverse=True) # ters sıralar





























