
#SAYILAR VE STRINGLERE GIRIS

9 #integer
9.2 #float
9+9
9*9
9/1

type(9)
type('hello ai era')


#STRINGLERE YAKINDAN BAKALIM


"123"
type("123")


print("a")

"a" + "b"

"a" "b"

"a" "-b"

"M" "-V" "-K"

"a" - "b" #calismaz

"A"*3

"A"/3


#STRING METODLARI 

#LEN: boyut bilgisi


#atama islemi
ds = "data scientist"
ds

len("ali")

len("daha uzun bir sey")

len("data scientist")
len(ds)
len("ds")

del ds
#len(ds)

a = 999999
b = 10

del a
#a*b


a = 999999
b = 10

#UPPER() & LOWER()


ds = "data scientist"

ds.upper()
BUYUK_DS = ds.upper()

BUYUK_DS

asd = BUYUK_DS.lower()


#replace()

ds = "data scientist"


len(ds)

ds.replace("a","e")

a = ds.replace("i","o")

a.upper()

#strip()


ds = " data scientist "
ds = "*data scientist*"
ds = "*ldata scientist*l"
ds = "l*data scientist*l"

ds.strip("l")


ds = "data scientist"


dir(ds)

ds.islower()

ds.isnumeric()


#DEGISKENLER

a = 9

c = a*6

c



#TYPE DONUSUMLERI
type(9)
type("ali")

#Kullanicidan bilgi almak icin
one = input()
two = input()

one + two

type(10.2)

int(10.2)

int(one)


int(one) + int(two)

float(10)


#PRINT

print("HELLO","AI")
print("HELLO","AI", sep = "_A_")
print('mehmet dedi ki "asdfsad"')

#SUBSTRINGS

a = "data scientist"
a[0:4]
a[5:14] #slicing


#DATA TYPES (VERI YAPILARI)

#Lists
#Tuples
#dictionary
#set

#Listeler
#Degisebilirdir.
#Siralidir.
#Kapsayicidir.


isimler = ["ali","veli"]

isimler[0]


isimler = [0,"ali","veli"]
liste = [9,1,2,3,4,5, isimler]


liste[6][1] 

liste[1:3]

liste = ["ai", "ds", "ml","sl"]

liste[0] = "AI"
liste

liste[1:3] = "DS", "ML"
liste

liste = liste + ["Kemal"]
liste


dir(liste)
#append
liste.append("Data")

liste

del liste[4]

liste.remove("Data")

#insert
liste.insert(5,"DL")

liste.insert(len(liste), "ai")
liste

#pop
liste.pop(3)

#count
liste.count("DS")

#copy
liste_yedek = liste.copy()

#extend
liste.extend(["a","b",10])
liste

#index
liste.index("ML")

#reverse
liste.reverse()

#sort
liste = [90,69,10,20]
liste.sort()
liste

#clear
liste.clear()

#Tuples
#siralidir
#degistirilemez 
#kapsayicidir


t = ("ali","veli", 1,2,3,4)

type(t)
t[1]
t[0:3]

t[0] = "a"


#Dictionary (Sozluk)

#key-value
sozluk = {"REG":"Regresyon"}


sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}


sozluk

sozluk["CART"]


sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}

sozluk["CART"]


sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE", 20],
          "CART" : ["SSE",30]}

sozluk["CART"]



sozluk = {"REG" : {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30},

          "LOJ" : {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30},
                   
          "CART" : {"RMSE": 10,
                   "MSE" : 20,
                   "SSE" : 30}}


sozluk["REG"]["SSE"]



sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}


sozluk["REG"] = "GBM"


#Setler ODEV.








#FONKSIYONLAR

print("a","b", sep = "_")
#?print

print()

len("asdas")


4**2


def kare_al(x):
    print(x**2)

kare_al(4)

def kup_al(x):
    print(x**3)

kup_al(8)


def carp(x,y):
    print(x*y)
        

carp(4,5)

def kare_al(x):
    print("Sayinin Karesi: " + str(x**2))



kare_al(4)

#on tanimli argumanlar

def carp(x, y = 1):
    print(x*y)
    
carp(5)    

#argumanların siralamasi

carp(y = 5, x = 4)
carp(x = 4, y = 5)


#Ne zaman fonksiyon yazilir?

#isi, nem, sarj
(40 + 25)/90

(24 + 76)/80

(12 + 43)/89

(12 + 43)/89

(12 + 43)/89


def direk_hesap(isi, nem, sarj):
    print((isi+nem)/sarj)


a = direk_hesap(24,78,98)
a
print(a)


#return


def direk_hesap(isi, nem, sarj):
    return (isi+nem)/sarj
    


direk_hesap(24,78,98)*5

a = direk_hesap(24,78,98)
a*5

#local ve global degiskenler
x = 10
y = 20

def carp(x, y = 1):
    return x*y

carp(3,4)


#local etki alanindan global etki alanini degistirmek

x = [] 

def eleman_ekle(y):
    x.append(y)
    

x

eleman_ekle(4)
x    
    
    
#KARAR & KONTROL YAPILARI (IF)

#boolean (true-false sorgulamaları)

5 == 4

sinir = 5000    
gelir = 4000    

gelir > sinir    
    
if gelir > sinir:
    print("Gelir sinirdan buyuktur")    
else:
    print("Gelir sinirdan buyuk degildir")


#elif    
    
sinir = 50000
gelir1 = 50000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler")
elif gelir1 < sinir:
    print("Uyari!") 
else:
    print("Takibe devam")    


#mini uygulama
sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
    print("Tebrikler!" + magaza_adi + " promosyon kazandiniz!")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir:" + str(gelir))
else:
    print("Takibe devam")

   
    
#DONGULER for 

maaslar = [1000, 2000,3000,4000,5000]    
maaslar
    
maaslar[0]
maaslar[1]    
maaslar[2]

for i in maaslar:
    print(i*3)
    
#dongu ve fonksiyonların beraber kullanimi
#amac yuzde 20 zam
    
1000*20/100 + 1000


maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]
maaslar[2]*20/100 + maaslar[2]

def yeni_maas(x):
    print(x*20/100 + x)


yeni_maas(2000)    



for i in maaslar:
    yeni_maas(i)


#mini uygulama
#if, for ve fonksiyonlari birlikte kullanmak    

    
maaslar = [1000,2000,3000,4000,5000]


def maas_ust(x):
    print(x*10/100 + x)

def maas_alt(x):
    print(x*20/100 + x)
    
    
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)


#break & continue
        
maaslar = [1000,2000,3000,4000]


for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)

 

for i in maaslar:
    if i == 3000:
        continue
    print(i)

#while

sayi = 1

while sayi < 9:
    sayi += 1
    print(sayi)


"9" + 1
ifade = "Merhaba! " 
ifade.strip("")



