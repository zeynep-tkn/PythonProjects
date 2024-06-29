#random modulu kullanilarak elde edilecek islemler

import random
print(""""
      1-Random sayi uretmek
      2-Random dizi uretmek""")
islem=int(input("Yapmak istediginiz islem satirini girin:"))

if islem==1: 
    print("0-1 arasi 10 random sayilar")
    for i in range(10):
        print(random.random())
    
    print("\n10-30 arasi 10 random sayilar")
    for i in range(10):
        print(random.uniform(10,30))
    
    print("\n1-5 arasi 10 tam sayi")
    for i in range(10):
        print(random.randint(1,5))   
    
    print("\n1-30 arasi ikiser artan 10 tam sayi")
    for i in range(10):
        print(random.randrange(1,30,2))

elif islem==2:
    print("Random eleman sec")  
    liste=["elma","armut","vişne","kiraz"]
    print(random.choice(liste))
    
    print("Listeyi random yaz")
    random.shuffle(liste)
    print(liste)