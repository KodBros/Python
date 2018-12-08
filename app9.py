class yeniSinif:
    def __init__(self,isim,numara,bakiye): # self mutlaka yazılmak zorunda
        self.isim = isim                   # bu metod (init) oluşturulacak nesnenin özelliklerini belirlememizi sağlıyor.
        self.numara = numara
        self.bakiye=bakiye
    def bilgileriGoster(self):
        print("İsim :",self.isim)
        print("Numara :",self.numara)
        print("Bakiye :",self.bakiye)
    def paraCekme(self,cekilenMiktar):
        kalan = self.bakiye - cekilenMiktar
        if kalan>0:
            print("Para çekme işlemi başarıyla gerçekleşti")
            print("Yeni Bakiyeniz :",kalan,"tl")
        else:
            print("Bakiyeniz",self.bakiye,"tl daha küçük bir miktar girin")
            self.paraCekme(int(input("Çekilecek miktar :")))
yeniNesne = yeniSinif ("Ali",123456789,100)
yeniNesne.bilgileriGoster()
yeniNesne.paraCekme(int(input("Çekilecek miktar :")))