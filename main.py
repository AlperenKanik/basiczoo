import tur, hayvanlar
import random

while True:
    menu = input("$$$-Hayvanat Bahçesine HOŞGELDİNİZ!-$$$\n "
                   "tür eklemek için A'ye tıklayın. \n "
                   "Öğrenci eklemek için B'ye tıklayın: \n"
                   "Çıkış için C'ya  tıklayınız: \n")

    if menu == "C" or menu == "c":
        print("##-ßß-CYA-###")
        break

    else:
        Sınıfİsmi = input("Hayvanın türünü giriniz: \n")

        if menu == "A" or menu == "a":
            zoo.Zoozz.ekle(zooz)

        elif menu == "C" or menu == "c":
            TasmaNO = random.randint(5001,9998 )
            HayvanAdi = input("Hayvanın adını giriniz: \n")
            HayvanTuru = input("Hayvanın türünü giriniz: \n")
            zoo.Zoo.ekle(Zoozz,TasmaNo, HayvanAdi, HayvanTuru)
