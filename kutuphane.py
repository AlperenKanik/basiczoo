import sqlite3

def login():
    while True:
        ogrencino = input("lütfen öğrenci numaranızı girin:")
        sifre = input("lütfen şifrenizi girin:")
        with sqlite3.connect("kutuphane.db") as db:
            cursor = db.cursor()
            findUser =("SELECT * FROM user WHERE ogrencino = ? And sifre = ?")
            cursor.execute(findUser,[(ogrencino),(sifre)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    print ("MERHABALAR"+i(2))
                    #programı kapatmaması için
                    break
            else: 
                print("yanlış kullanıcı adı veya şifre")
                again = input("tekrar denemek ister misiniz ?E/H")
                if again.lower() == "h":
                    print ("iyi günler")
                    time.sleep(1)
                    break


def newUser():
    found = 0
    while found == 0:
        ogrencino = input(" lütfen ögrenci numaranızı girin")
        with sqlite3.connect("kutuphane.db") as db:
            cursor = db.cursor()
        findUser=("SELECT * FROM user WHERE ogrencino = ?")
        cursor.execute(findUser,((ogrencino)))

        if cursor.fetchall():
            print("zaten bir üyeliğiniz mevcut")
        else:
            found = 1

        ad = input("adınız")
        soyad = input("soyadınız")
        sifre = input("sifre")

        insertData = '''INSERT INTO user(ogrencino,ad,soyad,sifre)
        VALUES(?,?,?,?)'''
        cursor.execute(insertData,[(ogrencino),(ad),(soyad),(sifre)])
        db.commit()

        newUser()
        
def menu():
    while True:
        print("BASKENT KUTUPHANESİ SİSTEMİNE HOSGELDİNİZ")
        menu =('''
        1 - ÜYE OL
        2- GİRİŞ YAP
        3- UYGULAMAYI KAPAT /n''')

        userChoice = input(menu)
        if userChoice =="1":
            newUser()

        elif userChoice =="2":
            login()
        elif userChoice =="2":
            sys.exit()
        else:
            print("yanlış giriş yaptınız")
menu()
