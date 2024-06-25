#Basit hesap makinesi
ilkSayi =int(input("İlk sayiyi girin:"))
ikinciSayi=int(input("İkinci sayiyi girin:"))
islem=input("""
Lütfen işlemlerden birini seçin
Toplama:+ , Çıkarma:- , Çarpma:* , Bolme:/ , Us alma:us """)

if   islem == "+":
    print("Sonuc:" +str(ilkSayi+ikinciSayi))
elif islem == "-":
    print("Sonuc:"+str(ilkSayi-ikinciSayi))
elif islem == "*":
    print("Sonuc:"+str(ilkSayi*ikinciSayi))
elif islem == "/":  
    print("Sonuc:"+str(ilkSayi/ikinciSayi))
elif islem == "us":
    print("Sonuc:"+str(ilkSayi**ikinciSayi))

