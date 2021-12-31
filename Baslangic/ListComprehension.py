# # liste = [1,2,3,4,5]
# # liste.append("Osman")
# # print(liste)

# # liste1 = [] # liste1 = list()

# # #Uzun Yol
# # for i in liste:
# #     liste1.append(i)
# # print(liste1)

# # #Kısa yol
# # liste3 = [i for i in liste]
# # print(liste3)



# liste = [3,4,5]

# liste1 = [i**2 for i in liste] 
# print(liste1)


# listt = [(1,2),(3,4),(5,6)]

# listt1 = [i*j for i,j in listt]

# print(listt1)

s = "string"

liste = [i*3 for i in s]
print(liste)
liste = []
listt = [(1,2),(3,4),(5,6)]

for i in listt:
    for j in i:
        liste.append(j)

print(liste)

# yukarıdakinin kısa hali budur.add()

liste2 = [x for i in listt for x in i]
print(liste2)




