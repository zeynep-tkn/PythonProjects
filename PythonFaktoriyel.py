#Sayinin faktoriyelini hasapla

sayi=int(input("Lütfen faktoriyelini hesaplamak istediğiniz sayıyı girin:"))
faktoriyel=1
for i in range(1,sayi+1):
   faktoriyel*=i
print(f"{sayi}! = {faktoriyel}")

