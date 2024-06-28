#ilk 10.000 sayısının kaç tanesi 3 ile başlar 7 ile biter
prime_list = list()
prime_list.append(2)

sayi=3

while True:
    prime= True
    for i in range(2,int(sayi**0.5)+1):
       if sayi %i==0:
           prime=False
           break
    if prime:
        prime_list.append(sayi)
        if len(prime_list)==10000:
            break
    sayi+=1
liste2=[]
for prime in prime_list:
    strprime=str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
        liste2.append(prime)
print(liste2)
print(len(liste2))