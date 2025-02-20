faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)   #vade degeri int e cevrildi sayi old ıcın cevirildi
#print(int(krediAdi)) #hatalı cunku tip str ınt olamıyor
faiz = str(faiz)
print(str(faiz))

vade = int(input("Lütfen istediğiniz vade sayisini giriniz:"))  #basına ınt koyulursada tur sıkıntısı olamaz
print(type(vade))   #str olur
#print(int(vade) + 12) tip str den int e cevrildi
vade = vade + 12

#string interpolation
#seçtiğiniz vade sonucu ortaya cıkan vade:
print("Seçtiğiniz vade sonucu ortaya çikan vade:" + str(vade))
print("Seçtiğiniz vade sonucu ortaya çikan vade: {vadeSayisi}".format(vadeSayisi=vade) )
print(f"Seçtiğiniz vade sonucu ortaya çikan vade: {vade}")

isim=input("isminizi giriniz")
isim="Nisa Nur"
metin = "merhaba {name}".format(name="Karaca")
print(metin)


#f-string
metin = f"hosgeldiniz {1+1}"     #f eklersek metin
print(metin)


#listeler #dizi
#döngüler
#fonksiyonlar

dizi= ["ihtiyac kredisi",10 ,5.2, True]
print(dizi)

krediler = ["ihtiyac kredisi", "tasit kredisi", "konut kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler))    #length
#print(krediler[3]) => hata verir

krediler.append("özel kredi")   #ekledi
print(krediler)

krediler.append("x kredisi")
print(krediler)

krediler.pop(0)     #siliyor index
pop(krediler)

krediler.append("tasit kredisi")
print(krediler)

krediler.remove("taşit kredisi")    #siliyo ilk olanı
print(krediler)

krediler.extend(["y kredisi", "z kredisi"])     #2 append yerine tekte kullanılır
print(krediler)

# for
# i=0 i<10

for i in range(10):     #i yi sıfırdan baslatıp 10 a kadar dongu calısır
    print("xx")
    print(i)

print("***************")
for i in range(5,10):    #5 (dahıl)ile baslayıp 10 a kadar yazdırır
    print(i)

print("****************")
for i in range(0,51,10):
    print(i)

print("****************")
#for i in range(0.1,0.5):
#print(i)
krediler = ["ihtiyac kredisi", "tasit kredisi", "konut kredisi"]
for i in krediler:
    print(kredi)
print("****************")
for i in range(len(krediler)):  # parantez içi 3
    print(krediler[i])  #3 defa calısacak
print("****************")

#sonsuz dongu
i = 0
while i < 10:   #programı ctrl c ile durdurmalısın yoksa durmuyor
    print("x") 
    i += 1  #i=i+1 
print("y")

print("****************")

while True:
    print("x")
    break   #dongu kırdı

print("********son dongu********")

i=0
while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "konut kredisi":
        break



#fonksiyonlar

fiyat = 100
indirim =20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)    #80

def sayHello(name):
    print(.f"Merhaba {name}")


calculate()
calculateWithParams(50,10)  #50-10
calculateWithParams(100,30)     #100-30
sayHello("nisa")    #merhaba nisa
sayHello("maya")
sayHello("deniz")


def calculateAndReturn(price, discount):
    return price-discount   #eksi ve return olma sebebi degısken olarak kullanabilme fırsatı saglaması
#return["1", "2"] cıktı =>['1', '2'] +10 olmazsa 
yeniFiyat = calculateAndReturn(200,50)   #sira onemli
print(yeniFiyat + 10)   #150

def calculateAndReturn(price, discount):
    print(price-discount)

def calculateAndReturn(price, discount):
    return price-discount


print("****************")
fonk1 = calculatePrice(100, 50)
fonk2 = calculatePrice(300, 100)
print(f"159. satir:{fonk1}")     #none ve print(f"159. satir:{fonk1+100}") =>error
print(f"160. satir:{fonk2}")     #200 ve print(f"160. satir:{fonk2+100}") =>error
print("****************")