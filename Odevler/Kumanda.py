import random
import time
from typing import Text

class Kumanda():


    def __init__(self,tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["trt"],kanal = "trt"):
        self.tvdurum = tv_durum
        self.tvses = tv_ses
        self.kanallistesi = kanal_listesi
        self.kanal = kanal

    def TvAc(self):
        if self.tvdurum == "Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon Açılıyor")
            self.tvdurum ="Açık"
    def TvKapa(self):
        if self.tvdurum == "Kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon Kapanıyor")
            self.tvdurum ="Kapalı"
    
    def SesAyarları(self):

        while True:
            cevap = input("Sesi azalt : '<' \nSesi artır : '> \nÇıkış : çıkış'")
            if cevap == ("<"):
                if self.tvses !=0:
                    self.tvses -= 1
                    print("Ses:",self.tvses)
                
            elif (cevap == (">")):
                if self.tvses !=32:
                    self.tvses += 1
                    print("Ses Artırılıyor",self.tvses)
            
            else:
                print("Ses Güncellendi",self.tvses)
                break
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor")
        time.sleep(1)

        self.kanallistesi.append(kanal_ismi)
        print("Kanal Eklendi")
    
    def RasgeleKanal(self):
        rasgele = random.randint(0,len(self.kanallistesi)-1)
        self.kanal =self.kanallistesi[rasgele]

        print("Şuanki kanal ",self.kanal)

    def __len__(self):
        return len(self.kanallistesi)
    
    def __str__(self):
        return " Tv Durumu : {} \n Tv Ses : {} \n Kanal Listesi : {} \n Şuanki Kanal : {} \n".format(self.tvdurum,self.tvses,self.kanallistesi,self.kanal)



print(""" 

Televizyon Uygulaması

1.Tv aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Sayısını Öğrenme

6.Rastgele Kanal Geçme

7.Televizyon Bilgileri

Çıkmak için 'q Basınız'


""")
kumanda = Kumanda()

while True:

    işlem = input("İşlemi seçiniz")

    if işlem == 'q':
        print("Programdan çıkıyot")
        break

    elif işlem == "1":
        kumanda.TvAc()
    elif işlem == "2":
        kumanda.TvKapa()
    elif işlem == "3":
        kumanda.SesAyarları()
    elif işlem == "4":
        
        kanal_isimleri = input("Kanal İsimlerini ',' Ayırarak Giriniz:")
        
        kanal_listesi = kanal_isimleri.split(",")

        for i in kanal_listesi:
            kumanda.kanal_ekle(i)
    elif işlem == "5":
        print("Kanal Sayısı:",len(kumanda))
    
    elif işlem == "6":
        kumanda.RasgeleKanal()
    elif işlem == "7":
        print(kumanda)
    else: 
        print("Geçersiz İşlem")




