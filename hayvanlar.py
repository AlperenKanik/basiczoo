import sqlite3

class hayvanlar:
    def __init__(self):
        self.con = sqlite3.connect("hayvanat_bahcesi.db")
        self.cursor = self.con.cursor()

    def ekle(self, Zooz, TasmaNo, HayvanAdi, HayvanTuru):
        self.cursor.execute("INSERT INTO {Zoo_z} VALUES(?,?,?)".format(Zoo_z = Zooz),
                            (TasmaNo, HayvanAdi, HayvanTuru))
hayvanlar = hayvanlar()
