sayi1 = input("1. Sayıyı yazın : ")
sayi2 = input("2. Sayıyı yazın : ")
print("Sayıların Toplamları : ",sayi1+sayi2) # Burada sayıları string şeklinde algılar bu yüzden yan yana yazacaktır.

sayi1 = int (input("1. Sayıyı yazın : "))
sayi2 = int (input("2. Sayıyı yazın : "))
print("Sayıların Toplamları : ",sayi1+sayi2) # Burada ise string olan bir veriyi int (tamsayı) yaptık.

yas = int (input("Yaşınız : "))
if yas<18:
    print("Yaşınız 18'den küçük.")
elif yas==18: # elif = else if . elif kullanılırsa ilk if doğru olduğunda program diğer if koşullarına (elif e)bakmaz
    print("Yaşınız 18.")
else:
    print("Yaşınız 18'den büyük.")

a=5
b=5
c=5
d=10
if  a==b and b==c: # tüm eşitliklerin doğru olması gerekir.
    print("a, b, c birbirine eşit.")
if  a==b or d==10: # yanlızca 1 eşitliğin doğru olması elif bloğunun içindeki komutların çalıştırılması için yeterlidir.
    print("a b'ye eşit yada d 10'a eşit.")
if (not (a>b)):
    print("a b'den büyük değildir.")