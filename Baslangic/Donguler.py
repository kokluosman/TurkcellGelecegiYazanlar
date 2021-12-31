#For Döngüleri

#Liste Üzerinde gezinme

liste = [1,2,4,5,6,5,4,8,9,10]
toplam =0
for i in liste:
    if (i%2)==0:
        print(i)
    else:
        toplam = toplam +1 
    
print("Kaç eleman bölünmüyor",toplam)

s = "Osman"

for i in s:
    print(i*3)

#Listlerde stringlerde for döngüsü ile gezinilebilir.

liste2 = [(1,2),(2,3),(3,4)]

for (i,j) in liste2:
    print("i : {}  ,  j : {}".format(i,j))

#Sözlükler üzerinde gezinmek

a = {"bir" :[1,2,3,4],"iki":[[1,2],[3,4],[5,6]],"üç":15 } # Sadece anahtarlar üzerinde gezinir.

for i in a:
    print(i)

for i in a.values():
    print(i)

for i in a.items(): # Liste içinde demet şeklinde yapı oluşturur.
    print(i)

for (i,j) in a.items(): # Liste içinde demet şeklinde yapı oluşturur.
    print(i,j)

# While Döngüsü

i =0 
while(i<10):
    print("İ'nin değeri",i)
    i += 1

#range() fonksiyonu

for i in range(1,20,2): # 3 parameter. Başlangıç bitiş ve artış miktarı
    print(i)    

#Break ve continue ifadeleri


#Döngülerin içinde kullanılır.


for i in liste2:
    if i == (2,3):
        break
    print(i)

#Continue ifadesi Az kullanılır am asen yinede fikir sahibi ol.
#Continue ile karşılarşırsa geri kalan işlemi yapmaz başa döner.

for i in range(0,11):
    if i == 3 or i == 5:
        continue
    print("İ : ",i)











































