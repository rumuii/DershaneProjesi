import sqlite3

con = sqlite3.connect("ProjeDershanem.db")

cursor = con.cursor()


def tabloolustur():
    cursor.execute(" CREATE TABLE IF NOT EXISTS tbl_ogrenci "
                   "(ad TEXT,"
                   "soyad TEXT,"
                   "numara INT,"
                   "email TEXT,"
                   "parola TEXT) ")
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_ogretmen "
                   "(ad TEXT,"
                   "soyad TEXT,"
                   "numara INT,"
                   "email TEXT,"
                   "brans TEXT"
                   "parola TEXT) ")
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_yonetici "
                   "(ad TEXT,"
                   "soyad TEXT,"
                   "numara INT,"
                   "email TEXT,"
                   "parola TEXT) ")
def degerekle():
    cursor.execute("INSERT INTO tbl_ogrenci VALUES ('Rumeysa','Ergen','5534540000','rumeysa@gmail.com','12345')")
    cursor.execute("INSERT INTO tbl_ogretmen VALUES('Ali Furkan','Zıvlak','5550000000','ali111@gmail.com','23456')")
    cursor.execute("INSERT INTO tbl_ogretmen VALUES('Onur','Mersinlioglu','5570000000','onur111@gmail.com','34567')")
    cursor.execute("INSERT INTO tbl_yonetici VALUES('Ali Furkan','Zıvlak','5550000000','ali111@gmail.com','23456')")
    con.commit()
    con.close()

tabloolustur()
degerekle()


