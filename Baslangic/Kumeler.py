#Setler Kümeler

#Sırasızdır(İndexsiz)
#Değerler Eşsizdir. Tekrar eden derğerlerden oluşamaz.add()
#Değiştirilebilir.
#Hız İstenilen yerlerde kullanılabilir.
#Aynı şeyler tekrarlamaz
# s = set()

# l = list([18,"a","ali",123])

# s = set(l)

# print(s)

# ahmet ="Ben gelmek ankara istanbul falan filan"

# a = set(ahmet)

# print(a)


#Eleman Ekleme ve Eleman Çıkarma


l = ["gelecegi","yazanlar"]

s=set(l)

# s.add("Gelecegegit")

# dir(s)
# print(dir(s))

# print(s)

# s.add("ile")

# s.remove("ile")
# #Eğer içinde silecek bişey yoksa hata dönmez
# s.discard("ali")

set1 = set([1,3,5])
set2 = set([1,2,3])

a=print(set1.difference(set2))

b=print(set2.difference(set1))

#İki farka aynı anda bakmak istersek buna bakacağız
set1.symmetric_difference(set2)



set1-set2 # Bu a ya ait
set2-set1 # Bu b ye ait

#Setlerde kesişim ve birleşim

#Kesişim
print(set1.intersection(set2))
print(set2.intersection(set1))
#Birleşim
print(set1.union(set2))
print(set2.union(set1))

set1.intersection_update(set2)

#Setlerde Sorgu İşlemleri
#Kod akışı içerisinde kesişimin boş olup olmadığı veya kapsar mı bu soruları sorgulamak gibi şeyler için kullanılır

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

print(set1.isdisjoint(set2)) # İki küme kesişimi boş mu?? //// False 

print(set1.issubset(set2))  # Set1 set2 nin alt kümesi midir ??? // True

print(set2.issuperset(set1)) # Set2 set1 i kapsıyormu ?? /// True


















