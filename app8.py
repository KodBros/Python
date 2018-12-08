dosya1 = open("dosya1.txt","w") # w , bir dosya kipidir. Program her çalıştığında dosyayı yeniden oluşturur.
                                # Dosyamız burada oluşturuldu şimdi içerisine bir şeyler yazalım.
dosya1.write("Merhaba Dünya\n") # w dosya kipi kullandığımız için buradaki stringi her değiştirdiğimizde eski yazdığımız string kaybolur.
dosya1.close() # Yazma işlemi bittikten sonra close metodu ile kapatırız.

dosya2 = open("dosya2.txt","a") # a dosya kipi bir önceki yazılanları silmez. append'in kısaltılmasından gelir.
dosya2.write("Merhaba Python\n") # Bu string'i silip başka bir şey yazdığımızda dosyaya yeni yazdığımız string'i yazar.
dosya2.write("Merhaba Java\n")
dosya2.close() # Yazma işlemi bittikten sonra close() kullanmayı unutmayın hata verir.

dosya1 = open("dosya1.txt","r")
yazilar = dosya1.read()
print(yazilar)
dosya1.close()

dosya2 = open("dosya2.txt","r")
for satirlar in dosya2:
    print(satirlar)

dosya2 = open("dosya2.txt","r")
dosya2.seek(3) # Belirli bir indexten başlatmak için seek() metodunu kullanırız (dosyadaki 3. indexten başlar)
yazilar2 = dosya2.read(9) # 9. index'e kadarki verileri okur.
print(yazilar2)
dosya2.close()

