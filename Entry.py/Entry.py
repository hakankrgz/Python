"""
from audioop import lin2adpcm, lin2alaw


print("Merhaba Güzel Dünya")
gün = 22
gidiş_ücreti = 18.25
dönüş_ücreti = 17.5
masraf = gün * (gidiş_ücreti + dönüş_ücreti)
print("-"*30)
print("calışılan gün sayısı\t:", gün)
print("işe gidiş ücreti\t:", gidiş_ücreti)
print("işten dönüş ücreti\t:", dönüş_ücreti)
print("-"*30)
print("AYLIK YOL MASRAFI\t:", masraf)
isim = "Hakan"
soyisim = "Karagöz"
işsiz = "MacOS"
şehir = "Afyonkarahisar"
print("","isim           :",isim,"\n",
         "soyisim        :", soyisim, "\n",
         "işletim sistemi:",işsiz,"\n",
         "şehir          :",şehir,"\n",
         sep="   ")
piSayisi=3.14
#float tipinde bir veri tipi
print("pi sayısı=", piSayisi)
rCm=2
#integer tipinde veri
alan=3.14*rCm**2
print("Alan=", alan)
#sonuç float tipinde
print("Yarıçapı 2 olan dairenin alanı ",alan,"cm 2 dir")
karmasikSayi=4+5j
print("Bir karmaşık sayı=", karmasikSayi+3j)
print(type(alan))
print(type(karmasikSayi))

metin1 = "merhaba "
metin2 = "mars"
print (metin1)
print(metin1 * 2)
print (metin1 + metin2)
A=len(metin1)
print("metin adlı değişkendeki değerin uzunlugu:",A)

metin="Merhaba Mars"
print(metin[0])
print(metin[4:7])
print(metin[8::])
print(metin[-2])
print(metin[:7])
print(metin[8:])
print(metin[0:8:2])
print(metin[-1])
print(metin[::-1])

sayi1=5
sayi2=10.556
metin1="1"
sayi3=4+5j
askerlikYaptiMi=True
print("1. değişkenin veri tipi: ",type(sayi1))
print("2. değişkenin veri tipi: ",type(sayi2))
print("3. değişkenin veri tipi: ",type(metin1))
print("4. değişkenin veri tipi: ",type(sayi3))
print("5. değişkenin veri tipi: ",type(askerlikYaptiMi))
listem=["Çınar", 24, "Mühendis", True]
print("6. değişkenin veri tipi: ",type(listem))
demet1=("Çınar", 24, "Mühendis", True)
print("7. değişkenin veri tipi: ",type(demet1))
sozluk={"adi":"Çınar","yasi":24,"meslekUnvanı":"Mühendis","askerlikDurumu":True}
print("8. değişkenin veri tipi: ",type(sozluk))
küme={1,5,9,11,20}
print("9. değişkenin veri tipi: ",type(küme))

metin1="5"
metin2="3"
print(metin1+metin2)
print(int(metin1)+int(metin2))

print()
print("-----------------------")
print()

piDegeri=3.14
print("Veri Tipi: ",type(piDegeri))
yariCap=5
daireninAlani=((piDegeri*2)*yariCap)
print("Dairenin Alanı (float)=", daireninAlani)
piDegeriInt=(int(piDegeri))
print("Int veri tipine dönüştürülen piDegeri: ", piDegeriInt)
daireninAlani=((piDegeriInt*2)*yariCap)
print("Dairenin alanı (int)=", daireninAlani)

print()
print("-----------------------")
print()

askerlikYaptiMi=True
print("Askerlik Yaptı Mı?",askerlikYaptiMi)
askerlikYaptiMiInt=int(askerlikYaptiMi)
print("Askerlik Yaptı Mı?",askerlikYaptiMiInt)
askerlikYaptiMiStr=str(askerlikYaptiMi)
print("Askerlik Yaptı Mı?", askerlikYaptiMiStr)
print(7//2)


ad1="fevzi"
ad2="Fevzi"
print(id(ad1))
print(id(ad2))

ad1="fevzi"
ad2="fevzi"
print(id(ad1))
print(id(ad2))

a=103
b=3
print("a&b=",a&b)
print("a|b=",a|b)
print("~a=",~a)
print("a^b=",a^b)

a=11
b=-10
print("a>>1=",a>>1)
print("b>>1=",b>>1)
a=5
b=-10
print("a<<1=",a<<1)
print("b<<1=",b<<1)

metin=dgwjdkşlas dapsokdlansdasdnlas dpoasndlaksdlşnsaşld saldnaskdjn s dalsdsadas das
das dasdşaslödişsdasd asdisad as
dasd asd
asdasdasdasdsa
print(metin)
print("Fevzi","ÖZEK")
print('Fevzi',"ÖZEK",45)
ad="Fevzi"
soyad='ÖZEL'
yas=45
print(ad,soyad,yas)

print("Pazartesi","Salı","Çareşamba","Perşembe","Cuma")
print("Pazartesi","Salı","Çarşamba","Perşembe","Cuma",sep="-"*3)
print("Pazartesi","Salı","Çarşamba","Perşembe","Cuma",sep="\n")

dosya=open("/Users/hakankaragoz/deneme.txt","w")
print("Ben Python. Monty Python", file=dosya)
dosya.close()

a=5
b=6
c=3
print("girdiğiniz {},{}ve{} değerlerinin toplamı {}dır.".format(a,b,c,a+b+c))


dilekçe=
tarih: {}
T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanlığına
Fakülteniz {} Bölümü dasdoaksdpğsadkas dasmdas dsadsalkdsac as d
dasdasdsadasodsa dsandpksamdkasmdalskmdkşas
tarih=input("tarih: ")
üniversite=input("üni adı: ")
fakülte=input("fakülte adı: ")
bölüm=input("bölüm adı: ")
print(dilekçe.format(tarih,üniversite,fakülte,bölüm))
print("\n*3")

print("Yarın Adana'ya gidiyorum.\n")
print('"book" kelimesi Türkçede "kitap" anlamına gelir.\n')
print("birinci satır\n")
print("ikinci satır\n")
print("üçüncü satır\n")
print("Bir\nİki\nÜç\nFevzi\t ÖZEK\nBir\tiki")

isim=input("İsminiz nedir?")
print("Merhaba")
yaş=input("Yaşınız: ")
print("Demek", yaş,"yaşındasın.")
print("Genç mi yoksa yaşlı mı olduğuna karar veremedim.")

çap=input("Dairenin çapı: ")
yarıçap=int(çap)/2
pi=3.14159
alan=pi*(yarıçap*yarıçap)
print("Çapı",çap,"cm olan dairenin alanı:",alan,"cm2'dir.")

gun1=int(input("1. Günü giriniz: "))
ay1=int(input("1. Ayı giriniz: "))
yil1=int(input("1. Yılı giriniz: "))

gun2=int(input("2. Günü giriniz: "))
ay2=int(input("2. Ayı giriniz: "))
yil2=int(input("2. Yılı giriniz: "))

if gun1<gun2:
    ay1-=1
    gun1+=30
if ay1<ay2
sayi=int(input("Sayı girin: "))
if sayi<0:
    print(sayi," sayısı negatiftir.")


i=int(input("Sayı gir:"))
if  i%2==0:
    print(i," Sayısı Çift")
else:
    print(i," Satı Tektir.")
"""""
sayi1=int(input("1. Sayı gir:"))
sayi2=int(input("2. Sayı gir:"))
if sayi1>sayi2:
    print(sayi1," büyük olandır")
else:
    print(sayi2," büyük olandır")

