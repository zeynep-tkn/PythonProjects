#liste elemanlarinin toplamini ve ort hesaplayan fonksiyon

def liste_ort(liste):
    toplam=sum(liste)
    adet=len(liste)
    ort=toplam/adet
    print("liste:",liste)
    print(f"listenin ortalaması ={ort}\n")

liste_ort([1,2,3,4,5])

#metni tamamen buyuk harfe ceviren fonksiyon

def buyukHarfeCevir(metin):
    a=metin.upper()
    return a

test=buyukHarfeCevir("ben python dilini iyi şekilde öğreniyorum")
print(f"{test}  metni buyuk harfe çevrilmiştir")


