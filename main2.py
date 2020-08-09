import sqlite3

with sqlite3.connect("kutuphane.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
ogrencino VARCHAR(20) NOT NULL,
ad VARCHAR(20) NOT NULL,
soyad VARCHAR(20) NOT NULL,
sifre VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO user(ogrencino,ad,soyad,sifre)
VALUES("21794986","Alperen","Kanık","123")
""")
db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
