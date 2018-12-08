yazi = "app6"
print(yazi.startswith("ap")) # String'in " " içinde yazdığımız string ile başlayıp başlamadığını
print(yazi.startswith("ba"))                                    # true yada false olarak geri döndürüyor.

print(yazi.endswith("p6")) # Yukardaki metodun tam tersini gerçekleştirir.
print(yazi.endswith("ta"))

print(yazi.replace("p","e")) # Stringteki p yazan yerleri e olarak değiştirdik.
print(yazi.replace("ap","pa")) # Stringteki ap yazan yerleri pa olarak değiştirdik.


liste = [1,2,3,4,5,6]
liste.append(7) # append , listenin sonuna bir eleman eklememizi sağlar.
liste.append("txt")
print(liste)

liste.pop(0) # pop , içine yazılan index'i listeden siler
liste.pop() # pop'un içi boş bırakılırsa sondaki elemanı siler
print(liste)