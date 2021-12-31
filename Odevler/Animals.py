
class Hayvanlar():
    
    def __init__(self, tür, yaş,üreme_tipi,beslenme_şekli):
        self.tür = tür
        self.yaş = yaş
        self.üremetipi = üreme_tipi
        self.beslenmesekli = beslenme_şekli

      
class Kopekler(Hayvanlar):

    def Cins(self,kuyruk_tipi):
        return "Kuyruk Tipi : {}".format(kuyruk_tipi)

kopekler = Kopekler("Alman Kurdu",10,"Eşeyli","Etçil")

kopekler.Cins("Dik")

