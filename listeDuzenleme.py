#Liste uzerinde yapilan degisiklikler
renkler = ["mavi","sarı","kırmızı"]
sayilar = [1,2,33,5,8,16]

print("""
Hoş geldiniz...
1-Uzunluk bul
2-Eleman ekle
3-Belirli indekse eleman ekle
4-Eleman sil
5-İkinci liste elemanlarini ilkine ekle
6-Sildiğin elemanı goster
7-Listeyi tersine cevir
8-Alfabetik sirala
9-Min, max elemani bul
10-Liste elemanlarini topla
11-Listeyi numaralandir
12-Eleman listenin icinde mi kontrol et
13-Elemanlari bagla, listeyi belli yerden bol
            """)
islem= int(input("Lutfen listenize yapmak istediginiz islemi girin:"))

if   islem == 1:
    print("Listenin uzunlugu:",len(renkler))

elif islem == 2:
    print("İlk hali:",renkler)
    renkler.append("pembe")
    print("Son hali:",renkler)

elif islem == 3:
    print("ilk hali:",renkler)
    renkler.insert(1,"SİYAH")
    print("Son hali:",renkler)

elif islem == 4:
    renkler.remove("mavi")
    print("Son hali:",renkler)

elif islem == 5:
    print(renkler)
    renkler.extend(sayilar)
    print(renkler)

elif islem == 6:
    print(renkler)
    silinen = renkler.pop()
    print("silinen:",silinen)
    print("son hali:",renkler)

elif islem == 7:
    print(renkler)
    renkler.reverse()
    print(renkler)

elif islem == 8:
    renkler.sort()
    print("Alfabetik sirali:",renkler)

elif islem == 9:
    print(sayilar)
    print("Min:",min(sayilar))
    print("Max:",max(sayilar))

elif islem == 10:
    print(sayilar)
    print("Toplam:",sum(sayilar))

elif islem == 11:
    print(list(enumerate(renkler)))

elif islem == 12:
    print(renkler)
    print("gri" in renkler)

elif islem == 13:
    print(renkler)
    stringRenk ="-".join(renkler)
    print("Birlestir:",stringRenk)
    renkler2=stringRenk.split("-")
    print("Parcala:",renkler2)

else:
    print("Lutfen uygun secimi yapın!")
