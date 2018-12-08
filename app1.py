#Açıklama satırı yazmak için #(sharp) sembolü kullanırız.
"""
...
...
Çok satırlı açıklamalarda bu açıklama satırı tipinide kullanabiliriz.
...
...
"""

a = 10
b = 10.8
c = "metin"
d = [1,2,3,4,5,"metin"]
e = (1,2,3,4,5,"metin")

f = {"Ahmet":5} # Bu kullanıma sözlük adı verilmektedir.
                # Sözlükler soldaki ifadeye karşılık olan değerleri sağdaki ifadeyle eşleştiriyor.
g = True

# Değişkenin tipini type() metodu ile görebiliriz.
print(type(a),",",a) # int tam sayılar için kullanılan veri tipidir.
print(type(b),",",b) # float ondalıklı sayılar için kullanılan veri tipidir.
print(type(c),",",c) # str = string yani metin tarzı verileri içerisinde barındırır.
print(type(d),",",d) # list = liste tipindeki veri türüdür.
print(type(e),",",e) # tuple = demet , liste ile arasındaki fark ise ;
                       # Listelerde veri ekleyip silme işlemi bulunurken tuple da yoktur.
                          # Listedeki index() metodu yoktur eleman aranamaz
                             # Fakat döngüler tuple da daha hızlı çalışır.

print(type(f),",",f) # dict veri tipi. dict = dictionary (sözlük).
print(type(g),",",g) # bool = boolean veri tipi. İçerisinde sadece True yada False değer tutar.





