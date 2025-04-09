import csv
import random
from datetime import datetime
import time
import mysql.connector as mysql


class AppliConso:

    def __init__(self, num_capteur):
        self.num_capteur = num_capteur
        self.connexion_bd_equipe = None
        self.connexion_bd_commune = None

    def connexion_bds(self):
        print("")
        print("**************************")
        print("** Se Connecter aux BDs **")
        print("**************************")
        print("")
        try:
            # print('MySQL / paramstyle: ' + mysql.paramstyle)
            self.connexion_bd_equipe = mysql.connect(
                host='fimi-bd-srv1.insa-lyon.fr',
                port=3306,
                user='', # acompleter
                password=' ',# acompleter
                database=' '  # acompleter
            )
            print(f"=> Connexion à ... établie...")
            self.connexion_bd_commune = mysql.connect(
                host='fimi-bd-srv1.insa-lyon.fr',
                port=3306,
                user=' ',# acompleter
                password=' ', # acompleter
                database=' ' # acompleter
            )
            print(f"=> Connexion à .... établie...")
        except Exception as e:
            print('MySQL [ERROR]')
            print(e)

    def ajouter_mesure(self, num_inventaire, date, valeur):
        try:
            cursor = self.connexion_bd_equipe.cursor()
            cursor.execute('INSERT INTO Mesure (numInventaire,dateMesure,valeur) VALUES (%s,%s,%s)', [num_inventaire, date, valeur])
            self.connexion_bd_equipe.commit()
        except Exception as e:
            print('MySQL [INSERTION ERROR]')
            print(e)

    def derniere_mesure_inseree(self):
        '''fonction qui retourne la date de la dernière mesure saisie dans la base de donnée de l'équipe
        '''
        cursor = None # acompleter
        cursor.execute('# acompleter')
        maxDateMesure = cursor.fetchall()
        return maxDateMesure[0][0]

    def inserer_nouvelles_mesures(self, max_date_mesure):
        now = datetime.now()
        cursor = None # acompleter
        cursor.execute('# acompleter')

        num_mesures = 0
        for (idMesure, numInventaire, dateMesure, valeur) in cursor:
            num_mesures += 1
            #ajouter la mesure dans la base de donnée de l'équipe

        affichage_now = now.strftime('%d/%m/%Y à %H:%M:%S')
        affichage_max_date_mesure = max_date_mesure.strftime('%d/%m/%Y à %H:%M:%S')
        print(f"{affichage_now} => Copie de {num_mesures} nouvelle(s) mesure(s) depuis la dernière mesure copiée du {affichage_max_date_mesure}")


#######################
# Programme principal #
#######################

instance_conso = AppliConso(0) #A completer avec le numéro du capteur affecté 
instance_conso.connexion_bds()

# obtenir la date de la dernière mesure copiée dans la BD de l'équipe
#dernier = instance_conso.derniere_mesure_inseree()
# chercher les nouvelles mesures dans la BD commune et les copier dans la BD de l'équipe
#instance_conso.inserer_nouvelles_mesures(dernier)

