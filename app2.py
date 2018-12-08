print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10//4) # Sonucun tam sayı kısmını verir.
print(10%4) # Bölme işlemindeki kalanı verir.

print("app2 "*5) # Stringten kaç tane yazılmasını istiyorsak o sayıyla çarparız.

a="app2"
print(a,": nin 0. indexinde ",a[0],"karakteri var.") # a stringinin 0. karakterini ekranda gösteririz.
print(a[0:3]) # 0. indexten 3. indexe kadar olan kısmı yazar.
print(a[1:]) # 1. indexten son indexe kadar olan kısmı yazar.
print(a[:2]) # ilk indexten 2. indexe kadar olan kısmı yazar.
print(a,": nin uzunluğu ",len(a)) # a stringinin kaç karakterden oluştuğunu len (length) metoduyla öğrenebiliriz.

b=[1,2,3,4,5]
print(b,": nin 0. indexinde ",b[0],"elemanı var.")
print(b[::2]) # ilk indexten son indexe kadar olan elemanları 2 şer atlayarak yaz
print(b,": nin uzunluğu ",len(b))

c={"Ali":15,"Ahmet":24}
print(c["Ali"],c["Ahmet"])


