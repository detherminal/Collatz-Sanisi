import time

# Çalıştırmak için bunu kopyalayın "python3 Collatz-Sanisi.py"

# Bütün sayıların denenmesini istiyorsanız bunu True yapınız
# Bütün sayıların denenmesini istemiyorsanız bunu False yapınız
ButunSayilariDene = False

# Hızlı mod istiyorsanız bu değişkeni True yapınız
# Hızlı mod istemiyorsaniz bu değişkeni False yapınız
HizliMod = True

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Başta girilen sayı
while True:
    if (ButunSayilariDene == False):
        sayi = (input("Başlangıç Tam Sayısını Giriniz: "))
        if (is_int(sayi)):
            sayi = int(sayi)
            break
        else:
            print("Lütfen Tam Sayı Giriniz.")
            time.sleep(1)
            continue

# Bütün Sayıları Dene Kontrolü
if (ButunSayilariDene):
    baslangicsayi = 1
    denenensayi = baslangicsayi
    sayi = denenensayi
    while True: # denenesayi
        time.sleep(0.5)
        print(str(denenensayi) + " Sayısı Deneniyor.")
        time.sleep(0.5)
        while True: # sayi denemesi
            if (sayi % 2) == 0:
                sayi / 2
                continue
            elif (sayi == 1):
                time.sleep(0.5)
                print(str(denenensayi) + " Sayısı Döngüye Girmiştir.")
                break
            else:
                sayi = (sayi * 3) + 1
        denenensayi = denenensayi + 1
        continue        
else:
    # Yavaş Mod Kontrolü
    if (HizliMod == False):
        print("İşlem Yapılmaya Başlanıyor")
        time.sleep(1)
        print(sayi)
        while True:
            # Sayı çift mi diye kontrol
            if (sayi % 2) == 0:
                sayi = sayi / 2
                print(sayi)
                time.sleep(0.2)
                continue
            # Sayı 1 olduysa ve döngüye girildiyse
            elif (sayi == 1):
                print("Döngüye Girildi!")
                break
                # Sayı çift değilse
            else:
                sayi = (sayi * 3) + 1
                print(sayi)
                time.sleep(0.2)
                continue
    else:
        print("İşlem Yapılmaya Başlanıyor")
        time.sleep(1)
        print(sayi)
        while True:
            # Sayı çift mi diye kontrol
            if (sayi % 2) == 0:
                sayi = sayi / 2
                print(sayi)
                time.sleep(0.01)
                continue
            # Sayı 1 olduysa ve döngüye girildiyse
            elif (sayi == 1):
                print("Döngüye Girildi!")
                break
            # Sayı çift değilse
            else:
                sayi = (sayi * 3) + 1
                print(sayi)
                time.sleep(0.01)
                continue
