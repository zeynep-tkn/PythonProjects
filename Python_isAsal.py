# Sayi asal mi kontrol et

sayi = int(input("Lütfen asal olup olmadığını kontrol etmek istediğiniz sayıyı girin:"))

if sayi <= 1:
    print("Sayı asal değildir")
else:
    i = 2
    while i < sayi:
        if sayi % i == 0:
            print("Sayı asal değildir")
            break
        i += 1
    else:
        print("Sayı asaldır")