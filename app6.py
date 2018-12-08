from socket import socket


def fonksiyon1():
    print("Ahmet")

fonksiyon1()

def fonksiyon2(isim):
    print(isim)

fonksiyon2("Mehmet")

def fonksiyon3(isim = "İsimsiz kişi"):
    print(isim)

fonksiyon3()
fonksiyon3("Ali")

def toplama(a,b):
    return a+b

sonuc = toplama(5,3)
print("Sonuç :",sonuc)
