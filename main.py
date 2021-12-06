import csv
import pandas
import sqlite3

def matiere(n):
     if n[0] == "M":
          cours = "Mathematiques"
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

def end():
     connexion.close()  # Déconnexion

def connexion():
     try:
          connexion = sqlite3.connect("database.db")  ## BDD dans le fichier
          curseur = connexion.cursor()  # Récupération d'un curseur
          return(curseur)
     except sqlite3.Error as error:
          print("\nUne erreur dans la connexion à la DBB...")


def recupDate(groupe,date):

     ### me plaît pas (refaire la connexion à chaque fois)
     connexion = sqlite3.connect("database.db")  ## BDD dans le fichier
     curseur = connexion.cursor()  # Récupération d'un curseur
     ### ------------------------------------------------
     date = "Semaine du " + date
     groupe = "G"+groupe
     curseur.execute("SELECT " + str(groupe) + " FROM colles WHERE field1 = ?", [date])
     colle = curseur.fetchone()
     colle = ''.join(colle)
     colle = colle.split()
     curseur.execute("SELECT prénom1 , prénom2, prénom3 FROM Groupes WHERE numero = ?", [groupe])
     return(colle)

def recupAllDate():
     ### me plaît pas (refaire la connexion à chaque fois)
     connexion = sqlite3.connect("database.db")  ## BDD dans le fichier
     curseur = connexion.cursor()  # Récupération d'un curseur
     ### ------------------------------------------------
     curseur.execute("SELECT field1 FROM colles ")
     date = curseur.fetchall()
     x = []
     for k in range(0,22):
          y = ''.join(date[k])
          x.append(y)
     return(x)

def recupColle(colle):
     ### me plaît pas (refaire la connexion à chaque fois)
     connexion = sqlite3.connect("database.db")  ## BDD dans le fichier
     curseur = connexion.cursor()  # Récupération d'un curseur
     ### ------------------------------------------------
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