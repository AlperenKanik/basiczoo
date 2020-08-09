mport sqlite3

class tur:
    def __init__(self):
        self.con = sqlite3.connect("hayvanat_bahcesi.db")
        self.cursor = self.con.cursor()

    def ekle(self, Zooz):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {Zoo_z}"
                            "(TasmaNo INT, "
                            "HayvanAdi TEXT, "
                            "HayvanTuru TEXT)".format(Zoo_z=Zooz))
Zoozz = Zoozz()
