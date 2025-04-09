import csv
import random
from datetime import datetime
import time
import mysql.connector as mysql


class AppliProd:

    def __init__(self, num_capteur):
        self.num_capteur = num_capteur
        self.connexion_bd_commune = None

    def connexion_bd(self):
        print("")
        print("**************************")
        print("** Se Connecter à la BD **")
        print("**************************")
        print("")
        try:
            # print('MySQL / paramstyle: ' + mysql.paramstyle)
            self.connexion_bd_commune = mysql.connect(
                host='fimi-bd-srv1.insa-lyon.fr',
                port=3306,
                user=' ', # a completer
                password=' ', # a completer
                database=' ' # a completer
            )
            print("=> Connexion a ... établie...")
        except Exception as e:
            print('MySQL [ERROR]')
            print(e)

    def ajouter_mesure(self, num_inventaire, date, valeur):
        try:
            cursor = self.connexion_bd_commune.cursor()
            cursor.execute('INSERT INTO Mesure (numInventaire,dateMesure,valeur) VALUES (%s,%s,%s)', [num_inventaire, date, valeur])
            self.connexion_bd_commune.commit()
        except Exception as e:
            print('MySQL [INSERTION ERROR]')
            print(e)

    def produire_mesures(self):
        while True:  # boucle infinie
            date_mesure = None # a completer
            valeur = None #valeur aléatoire dans la fourchette [0..20]

            affichage_date_mesure = date_mesure.strftime('%d/%m/%Y à %H:%M:%S')
            print(f"{affichage_date_mesure} => Ajout d'une mesure: {valeur:.2f}")
            #poser une mesure dans la base de données

            delai = 0 #calculer un délai aléatoire entre 30 et 60 s
            print(f"Prochaine mesure dans {delai}s")
            time.sleep(delai)


#######################
# Programme principal #
#######################

instance_prod = AppliProd(0) # remlplacer 
instance_prod.connexion_bd()

# lancer la boucle infinie de production de données
#instance_prod.produire_mesures()

