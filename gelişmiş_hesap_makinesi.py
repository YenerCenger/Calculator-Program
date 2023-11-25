from matematik import *
from time import *
print("""
********************************************************************************
Hesap Makinesi Programı

Bu program ile aklınıza gelen her işlemi yapabilirsiniz.

Programdan Çıkmak için "q" tuşunu tuşlayınız.

İşlemler:

1-Toplama              6-Bölen Bulma                        11-Mutlak Değer

2-Çıkarma              7-Asal Sayı mı?                      12-Bölümden Kalan Bulma

3-Çarpma               8-Üs Alma                            13-Ebob

4-Bölme                9-En Yakın Küçük Sayıya Yuvarla      14-Ekok

5-Faktöriyel           10-En Yakın Büyük Sayıya Yuvarla     15-Logaritma Bulma

********************************************************************************
""")


while True:
    işlem = input("Lütfen Yapmak İstediğiniz İşlemi Seçin:")

    if işlem == "q":
        print("Hesap Makinesi Programından Çıkılıyor")
        sleep(0.5)
        break

    elif işlem =="1":
        sleep(0.5)
        toplam = 0
        while True:
            a = input("Toplamak İstedğiniz sayıları Girin:")
            sleep(0.5)
            if a == "q":
                print("Bu Sayıların Toplamı:",toplam)
                break
            else:
                a = int(a)
                toplam += a

    elif işlem == "2":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("{} sayısından {} sayısını çıkarınca sonuç: {}".format(a,b,çıkarma(a,b)))

    elif işlem == "3":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("Bu İki Sayının Çarpımı:",çarpma(a,b))

    elif işlem == "4":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("Bu İki Sayının Bölümü:", bölme(a,b))

    elif işlem == "5":
        sleep(0.5)
        a = int(input("Faktöriyelini Bulmak İstediğiniz Sayıyı Girin:"))
        sleep(0.5)
        print("Bu sayının faktöriyeli:",faktöriyel(a))

    elif işlem == "6":
        sleep(0.5)
        a = int(input("Bölenlerini Bulmak İstediğiniz Sayıyı Girin:"))
        sleep(0.5)
        print("Bu Sayının Bölenleri:",bölen(a))

    elif işlem == "7":
        sleep(0.5)
        a = int(input("Asal Olup Olmadığını Öğrenmek İstediğiniz Sayıyı Girin:"))
        sleep(0.5)
        if asal_sayı(a) == True:
            print("Asal Sayı")
        else:
            print("Asal Sayı Değil")

    elif işlem == "8":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("{} üssü {} = {}:".format(a,b,üs_alma(a,b)))

    elif işlem == "9":
        sleep(0.5)
        a = float(input("Sayıyı Girin:"))
        sleep(0.5)
        print("Bu Sayıdan Küçük En Büyük Sayı:",taban(a))

    elif işlem == "10":
        sleep(0.5)
        a = float(input("Sayıyı Girin:"))
        sleep(0.5)
        print("Bu Sayıdan Büyük En Küçük Sayı:", tavan(a))

    elif işlem == "11":
        sleep(0.5)
        a = int(input("Mutlak Değeri Bulunacak sayıyı Girin:"))
        sleep(0.5)
        print("Bu sayının Mutlak Değeri:",mutlak_değer(a))

    elif işlem == "12":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("{} sayısını {} sayısına bölününce kalan: {}".format(a,b,bölüm_kalan(a,b)))

    elif işlem == "13":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("Bu İki Sayının Ebobu:",ebob(a,b))

    elif işlem == "14":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("Bu İki Sayının Ekoku:", ekok(a, b))

    elif işlem == "15":
        sleep(0.5)
        a = int(input("İlk sayıyı Girin:"))
        sleep(0.5)
        b = int(input("İkinci sayıyı Girin:"))
        sleep(0.5)
        print("Bu İki Sayının logaritması:",log(a,b))

    else:
        print("Geçersiz İşlem")

