import random
sayi = random.randint(1,100) # 1 ile 100 arasında rastgele sayı üretmenin yolu...

def sayiTahmin(tahmin):
    while tahmin!=sayi:
        if tahmin < sayi:
           print("Sayı daha büyük tekrar dene :)")
           tahmin = int(input("Tahmin et : "))
        else:
            print("Sayı daha küçük tekrar dene :)")
            tahmin = int(input("Tahmin et : "))
    print("Sayıyı bildiniz.")

tahmin = int(input("Tahmin et : "))
try:
    sayiTahmin(tahmin)
except:
    print("Lütfen sadece sayı girin")
    sayiTahmin(tahmin)
