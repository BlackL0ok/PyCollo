# Import des noms du module
from tkinter import *
from backend import *

# Création d'un objet "fenêtre"
fenetre = Tk()

# configuration de la fenetre:
fenetre.geometry("500x140")
fenetre.minsize(500,140)
fenetre.maxsize(500,140)
fenetre.config(background="#272424")

# Affichage du titre
fenetre.title("Pycollo")


def recherchedate():
    ## Création de la fenetre réponse:
    def create():
        x = recupdata()
        z = recupDate(x[0], x[1])
        y = recupColle(z)
        ß = []
        for k in range(0, len(y), 3):
            texte = y[k] + ' '
            texte += y[k + 1] + ' '
            texte += y[k + 2]
            ß.append(texte)
        output = Toplevel(fenetre, bg='#272424')
        output.minsize(500, 140)
        output.maxsize(500, 140)
        espace = Label(output, text='', bg='#272424',foreground="#ffffff")
        espace.pack()
        for k in range(0, len(z)):
            cours = matiere(z[k])
            text_fin = cours + ' : ' + ß[k]
            text1 = Label(output, text=text_fin, bg='#272424',foreground="#ffffff")
            text1.pack()
        output.mainloop()
        return ()
    # fonction pour espacer les textes
    def espace(fenetre, row, column):
        label = Label(zoneMenu, text='', bg='#272424')
        label.grid(row=row, column=column)
    # fonction de qui donne la date et le groupe saisie
    def recupdata():
        x = []
        y = resultat_sbox_g.get()
        x.append(y)
        y = resultat_sbox_d.get()
        x.append(y)
        return (x)

    # Ajout des autres widgets
    zoneMenu = Frame(fenetre, borderwidth=3, bg='#272424')
    zoneMenu.grid(row=0,column=1,padx="40")

    espace(zoneMenu,0,0)
    groupeTxt = Label(zoneMenu, text='Groupe :',width='20',bg='#272424',foreground="#e8e5e5")
    groupeTxt.grid(row=1, column=1)

    # Espace de la spinBox:
    espace(zoneMenu,2,0)

    # Création de Spinbox Groupe:
    resultat_sbox_g = StringVar(value=0)
    gsbox = Spinbox(zoneMenu,from_=1,to=13,textvariable=resultat_sbox_g,bg='#272424',foreground="#e8e5e5")
    gsbox.grid(row=2,column=1)

    espace(zoneMenu,2,3)
    espace(zoneMenu,1,2)

    #Création de la Spinbox Semaine:
    date_jjmm = []
    date = recupAllDate()
    for k in range(0,22):
        date_jjmm.append(date[k][11:])
    resultat_sbox_d = StringVar(value=0)
    ssbox = Spinbox(zoneMenu,value=date_jjmm,textvariable=resultat_sbox_d,bg='#272424',foreground="#e8e5e5")
    ssbox.grid(row=2,column=3)

    # Création du Lbael semaine
    groupeTxt = Label(zoneMenu, text='Semaine du :',width='20',bg='#272424',foreground="#e8e5e5",)
    groupeTxt.grid(row=1, column=3)

    espace(zoneMenu,5,2)

    ## Button de check
    checkB = Button(zoneMenu, text='check',command=create,bg='#272424',foreground="#e8e5e5")
    checkB.grid(row=6,column=2)


recherchedate()






# Démarrage de la boucle Tkinter (à placer à la fin !!!)
fenetre.mainloop()