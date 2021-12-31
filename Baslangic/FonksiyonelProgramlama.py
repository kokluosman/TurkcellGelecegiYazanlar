#Yan Etkisiz Fonksiyonlar (Pure Functions)

# a = 5

# def impure_sum(b):
#     return a+b

# def pure_sum(a,b):
#     return a+b

# print(impure_sum(6))

# İsimsiz Fonsiyonlar

# def old_sum(a,b):
#     return a+b

# old_sum(3,4)

# new_sum = lambda a,b : a+b

# liste = [("b",3),("a",8),("d",12),("c",1)]

# # Buradaki indexleri sıraladı
# sorted(liste, key=lambda x : x[1])

# # Vektörel operasyonlar


# # a = [1,2,3,4]
# # b = [2,3,4,5]

# # ab = []

# # for i in range(0,len(a)):
# #     ab.append(a[i]*b[i])


# # MAP FILTER REDUCE

# a = [1,2,3,4,5]

# for i in a:
#     print(i+10)

# #Map fonksiyonu verilen bir vektörün içerisinde belirli bir fonksiyonu çalıştırma imkanı verir.

# list(map(lambda x : x +10 , a))

# FILTER fonksiyonu iteratif nesne alır. Başka iteratif nesne oluşturulur. İteratif nesne içerisinde aradığı şartlar filtrelenir

# liste = [1,2,3,4,5,6,7,8,9,10]

# print(list(filter(lambda x : x % 2 ==0,liste)))

#REDUCE fonksiyonu indirgeme işlemi yapar.değerler ile ilgili işlem yapmak istersen kullanılır

from functools import reduce


liste = [1,2,3,4]

reduce(lambda a,b : a+b,liste)














