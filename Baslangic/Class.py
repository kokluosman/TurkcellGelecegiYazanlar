# class Araba():
#     model = "Renault Megane"
#     renk = "Gümüs"
#     BeygirGucu = 110
#     SilindirSayisi = 4

# araba1 = Araba()

# Araba2 = Araba()

# araba1.model

#Sınıfların Kullanılma Mantığı Burada Başlıyor Kanks (İnİt Fonksiyonu önemli)

# class Araba:
#     #Varsayılan değer olarak fonksiyonlardaki gibi classlarda da default değer girilebilir.
#     def __init__(self,model,renk,beygir,silindir):
#         self.model = model
#         self.renk = renk
#         self.beygir = beygir
#         self.silindir = silindir

# araba = Araba()

# araba.model = "Renault Megane"
# araba.renk = "Gümüs"
# araba.beygir = 190
# araba.silindir = 8
  
#Sınıf İçinde Metod tanımlama Nasıl olabilir ona bakacağız

class Developer():
    def __init__(self, name, age,number,price,language):
        self.name = name
        self.age = age
        self.number = number
        self.price = price
        self.language = language
    def ShowTheInfo(self):
        print(""" 
        Yazılımcı objesinin Özellikleri
        İsim {}
        Yaş {}
        Numara {}
        Maaş {}
        Bildiği Diller {}
        """.format(self.name,self.age,self.number,self.price,self.language))

    def zamyap(self,ZamMiktari):
        print("Zam Yap")
        self.price = self.price + ZamMiktari
    
    def Dil(self,NewLanguage):
        print("Dil Ekleniyor")
        self.language.append(NewLanguage)


    
    
yazılımcı = Developer("Osman",25,5077919043,6500,["Python",".Net","Labview","Java","Matlab"])

yazılımcı.zamyap(300)
yazılımcı.Dil("GoLang")
yazılımcı.ShowTheInfo()





















