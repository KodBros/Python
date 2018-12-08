i = 1
while i<=10:
    print(i)
    i += 1

print()

j = 0
while j<=50:
    if j==30:
        break # break komutu döngüyü sonlandırır
    print(j)
    j += 10

print()

x = 1
while x<=10:
    if x==3 or x == 5:
        x+=1
        continue # program continue komutuna geldiğinde altındaki kodlara bakmaz ve döngüde bir sonraki duruma geçer.
    print(x)
    x += 1

