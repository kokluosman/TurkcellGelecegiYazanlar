"""
liste = list()

for i in range(1,101):
    if i%3 ==0:
        liste.append(i)
    else:
        pass
print(liste)

"""

liste = [i for i in range(1,101) if i % 2 == 0]

print(liste)


