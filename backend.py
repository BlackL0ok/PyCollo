import csv,pandas,sqlite3,datetime,calendar

def connexion():
     connexion = sqlite3.connect("database.db")  ## BDD dans le fichier
     curseur = connexion.cursor()  # Récupération d'un curseur
     return(curseur)

def matiere(n):
     if n[0] == "M":
          cours = "Mathematique"
     elif n[0]  == "A":
          cours = "Anglais"
     elif n[0] == "P":
          cours = "Physique"
     elif n[0] == "I":
          cours = "TP_Info"
     elif n[0] == "F":
          cours = "Francais"
     elif n[0] == "S":
          cours = "Sciences_Industrielles"
     return(cours)

def recupDate(groupe,date):

     curseur = connexion()
     date = "Semaine du " + date
     groupe = "G"+groupe
     curseur.execute("SELECT " + groupe + " FROM colles WHERE field1 = ?", [date])
     colle = curseur.fetchone()
     colle = ''.join(colle)
     colle = colle.split()
     curseur.execute("SELECT prénom1 , prénom2, prénom3 FROM Groupes WHERE numero = ?", [groupe])
     return(colle)

def recupAllDate():
     curseur = connexion()
     curseur.execute("SELECT field1 FROM colles ")
     date = curseur.fetchall()
     x = []
     for k in range(0,22):
          y = ''.join(date[k])
          x.append(y)
     return(x)

def recupColle(colle):
     curseur = connexion()
     liste1 = []
     for k in range(1,len(colle)+1):
          cours = matiere(colle[k-1])
          edt = colle[k-1]
          curseur.execute("SELECT prof, date, salle FROM calendrier WHERE matiere = ?", [colle[k-1]])
          info = curseur.fetchone()
          for x in range (1,4):
               info = list(info)
               liste1.append(info[x-1])
     return(liste1)


def dateAuto():
     date = datetime.date.today()    ## recupere la date
     jour = date.isoweekday()
     date = str(date)
     if int(date[5:7]) < jour:
          new_month = int(date[5:7]) - 1
          new_date = date.replace(date[5:7],str(new_month))
          nbr_jour = calendar.monthrange(int(date[0:4]),int(date[5:7]))
          nbr_jour = nbr_jour[1]
          jour_restant = jour - int(date[5:7])
          nbr_jour = nbr_jour - jour_restant
          date = new_date.replace(date[8:],str(nbr_jour))
     else:
          if int(date[8:]) < 10:
               x = int(date[9:]) - (jour - 1)
               lundi = '0'+str(x)
          else:
               lundi = +str(int(date[8:])+(jour-1))
          date = date[:8] + lundi
     date = date.replace('-','/')
     JJ = date[8:]
     MM = date[5:7]
     date = date.replace(JJ,MM)
     date = date.replace(MM, JJ,1)
     return(str(date[5:]))
