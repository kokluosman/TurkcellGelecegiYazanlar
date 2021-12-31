# #Iterator for da listelerde görülür.

# #__ıter__ ve __next__ tanımlanmalıdır.

# liste = [1,2,3,4,5,6,7,8,9,0]
# iterator = iter(liste)
# print(iterator)

# next(iterator)

# class Kumanda():
#     def __init__(self,kanal_listesi):
#         self.kanal_listesi = kanal_listesi
#         self.index = -1

#     def __iter__(self):
      
#       return self
#     def __next__(self):
#         self.index += 1
#         if self.index<len(self.kanal_listesi):
#             return self.kanal_listesi
#         else:
#             self.index=-1
#             raise StopIteration
# kumanda = Kumanda(["Atv","Trt","Fox","Star","Bloomberg"])
# iterator = iter(kumanda)


# print(next(iterator))

# Generator iterable obje oluşturmak için kullanılır. Bellekte herhangi bir yer kaplamaz.
# !!!!!!!!!!!!!!!!!! ÖNEMLİ !!!!!!!!!!!!!!!!!!!!!!!!!!!

def kare():
    liste = list()
    for i in range(1,6):
        liste.append(i**2)
    
    return liste

print(kare())

def kareal():
    for i in range(1,6):
        yield i**2

generator = kareal()
print(generator)

iteratoe = iter(generator)
print(next(iteratoe))

liste = [i * 3 for i in range(5)]


generator1 =(i * 3 for i in range(5))

iter(generator1)
print(next(generator1))






