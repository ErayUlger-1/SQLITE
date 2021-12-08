import function
import sqlite3
db=sqlite3.connect('odevdeneme.db')

imlec=db.cursor()
kmt="CREATE TABLE IF NOT EXISTS veriler(katagori,takım,oyuncu)"
imlec.execute(kmt)
"""
kmt="INSERT INTO veriler VALUES('Futbol','Türkiye','Yusuf')"
imlec.execute(kmt)
"""

#db.commit()
"""
kmt="Select * from veriler"
imlec.execute(kmt)
kayıtlar=imlec.fetchall()
print(kayıtlar)
"""
"""
kmt="Select * from veriler where oyuncu=?"
imlec.execute(kmt,('Yusuf',))
kayıt=imlec.fetchone()

print("Katagori : "+str(kayıt[0]))
print("Takım : "+str(kayıt[1]))
print("Oyuncu : "+str(kayıt[2]))

kmt="select * from veriler "
imlec.execute(kmt)
kayıtlar=imlec.fetchmany(4)
print(kayıtlar)

kmt="Select * from veriler "
imlec.execute(kmt)

for kayıt in range(3):
    print(imlec.fetchone())
    """

kmt="Delete from veriler where oyuncu = ?"
imlec.execute(kmt,('Burak',))
db.commit()
"""
kmt="Select * from veriler"
imlec.execute(kmt)
kayıtlar=imlec.fetchall()
print(kayıtlar)
"""



kmt="Select * from veriler"
kayıtlar=function.listele(db,kmt).fetchall()
print(kayıtlar)

db.close()




