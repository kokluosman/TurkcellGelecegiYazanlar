#Aşağı in demek   \n
print("Ahmet\nYapma\nDayı")

#Boşluk bırak 1 tab kadar     \t

print("Ahmet\tyapmadayı")

#type() function İçine girilen değerin tipini döndürür. 

a= 5
print(type(a))


#Print function parameters

print(3,4,5,sep="\n") # Bunun defautl değeri boşluk karakteridir.Sen sepe ne verirsen onu alır.

print(*"Ahmet") # HEr birini ayırarak koyar.

#Formatlama

a = 5.135
b = 7.145 

print("{}+{} toplamı {}".format(a,b,(a+b)))

print("{1}+{0} toplamı {2}".format(a,b,(a+b)))

print("{:.2f}+{:.3f} toplamı {}".format(a,b,(a+b)))








