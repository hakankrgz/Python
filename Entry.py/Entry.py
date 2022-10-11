from traceback import print_tb


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