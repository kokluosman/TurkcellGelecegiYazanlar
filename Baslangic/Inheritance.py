#Miras Alma Bunu Zaten Biliyorsun

# Dir fonksiyonu nesnelerin özellikleri hakkında bize nasihat verir.

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalıian Sınıfın init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgileriGoster(self):
        print("Çalışan Bilgileri Gösteriliyor")

        print("İsim : {} \n Maaş : {} \n Departman : {}".format(self.isim,self.maaş,self.departman))

    def DepartmanDegistir(self,YeniDepartman):
        print("Departman Değiştiriliyor")
        self.departman = YeniDepartman

class Yonetici(Çalışan):
    def ZamMiktari(self, miktar):
        print("Zam Yapılıyor")
        self.maaş = self.maaş + miktar



#Overriding veya iptal Etme (Bir metodu override edersek kendi tanımladığımız yerdeki metod çalışır.)



class Yonetici(Çalışan):
    def __init__(self, isim, maaş, departman , kisiSayisi):
      self.isim = isim
      self.maaş = maaş
      self.departman = departman
      self.kisiSayisi = kisiSayisi

    def ZamMiktari(self, miktar):
        print("Zam Yapılıyor")
        self.maaş = self.maaş + miktar



yonetici = Yonetici("Osman",5500,"Bilişim")
yonetici.ZamMiktari(1000)
yonetici.DepartmanDegistir("İnsan Kaynakları")
yonetici.bilgileriGoster()

#Super Anahtar Kelimesi


class Yonetici(Çalışan):
    def __init__(self, isim, maaş, departman , kisiSayisi):
      super().__init__(isim,maaş,departman)
      self.kisiSayisi = kisiSayisi

    def ZamMiktari(self, miktar):
        print("Zam Yapılıyor")
        self.maaş = self.maaş + miktar





















