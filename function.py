def listele(database,liste):
    imlec=database.cursor()
    kmt=liste
    imlec.execute(kmt)
  
    return imlec

def SorgulamaIslemleri(database,sorgu):
    imlec=database.cursor
    kmt=sorgu
    imlec.execute(kmt)
    return imlec