class Kitap():

    def __init__(self,name,yazar,sayfa,tur):
        self.name = name
        self.yazar = yazar
        self.sayfa = sayfa
        self.tur = tur
          
    def __str__(self): 
        # Return ile string dönmesi gerekir
        return " İsim : {} \n Yazar : {} \n Sayfa : {} \n Tür : {} ".format(self.name,self.yazar,self.sayfa,self.tur)

    def __len__(self):
        return self.sayfa
        # Del metodu
    def __del__(self):
        print("Kirap Objesi Siliniyor")
        



kitap = Kitap("Satranç","Stephen zweig",80,"Roman")
print(len(kitap))
print(kitap)


