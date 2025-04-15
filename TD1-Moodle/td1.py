# Python built-in Packages
import csv
import json
import random
from datetime import datetime
from inspect import currentframe
import mysql.connector as mysql
# Package MySQL Connector >> pip install mysql-connector-python
# import mysql.connector as mysql


def lire_fichier_csv(chemin_vers_fichier):

    print("")
    print(f"Lecture du fichier CSV: {chemin_vers_fichier}")

    nb_lignes = 0
    somme = 0.0

    with open(chemin_vers_fichier, 'r', encoding='utf-8') as fichier:
        reader = csv.reader(fichier, delimiter=';', quotechar='"')
        for ligne in reader:
            nb_lignes += 1
            print(f"ligne = {ligne}")
            numero = int(ligne[0]) # à compléter
            mesure = float(ligne[1])
            somme += mesure  # à compléter
            print(f"Le capteur n°{numero} a mesuré {mesure}")

    print(f"Nombre de Lignes: {nb_lignes}")
    moyenne = somme/nb_lignes
    print(f"Moyenne: {moyenne:.2f}")


def ecrire_fichier_csv(chemin_vers_dossier):

    print("")
    print(f"Écriture du fichier CSV")

    maintenant = datetime.now()
    print(maintenant)
    print(f"Maintenant: " + maintenant.strftime('%d/%m/%Y %H:%M:%S (+%fns)'))

    nom_fichier = "nombres-output_" + str(maintenant.strftime('%Y%m%d_%H%M%S')) +".csv" # à compléter, sans oublier le ".csv"
    chemin_vers_fichier = chemin_vers_dossier + nom_fichier

    print(f"Fichier CSV: {chemin_vers_fichier}")

    with open(chemin_vers_fichier, 'w', encoding='utf-8') as fichier:
        writer = csv.writer(fichier, delimiter=';', quotechar='"')
        for i in range(250):
            nombre = random.uniform(0, 100.0)
            rang = i
            nombre_formate = round(nombre, 2)
            writer.writerow([rang, nombre_formate])

    print(f"Écriture terminée")


def ouvrir_connexion_bd():
    print("")
    print("***********************")
    print("** Connexion à la BD **")
    print("***********************")

    connexion_bd = None
    try:
        connexion_bd = mysql.connect(
                host="fimi-bd-srv1.insa-lyon.fr",
                port=3306,
                user="G223_B",      # à compléter
                password="G223_B",  # à compléter
                database="G223_B_BD3"   # à compléter
            )
    except Exception as e:
        if type(e) == NameError and str(e).startswith("name 'mysql'"):
            print("[ERROR] MySQL: Driver 'mysql' not installed ? (Python Exception: " + str(e) + ")")
            print("[ERROR] MySQL:" +
                  " Package MySQL Connector should be installed [Terminal >> pip install mysql-connector-python ]" +
                  " and imported in the script [import mysql.connector as mysql]")
        else:
            print("[ERROR] MySQL: " + str(e))

    if connexion_bd is not None:
        print("=> Connexion établie...")
    else:
        print("=> Connexion échouée...")

    return connexion_bd


def fermer_connexion_bd(connexion_bd):
    print("")
    print("Fermeture de la Connexion à la BD")

    if connexion_bd is not None:
        try:
            connexion_bd.close()
            print("=> Connexion fermée...")
        except Exception as e:
            print("[ERROR] MySQL: "+str(e))
    else:
        print("=> pas de Connexion ouverte")


def afficher_liste_capteurs(connexion_bd):
    print("")
    print("Liste des Capteurs:")
    cursor = connexion_bd.cursor()
    cursor.execute("SELECT * FROM Capteur")   # à compléter
    for (bim, bam, boum) in cursor:   # à compléter
        print(f"{bim} @ {bam} => {boum}")   # à compléter


def ajouter_mesures_depuis_fichier_csv(connexion_bd, chemin_vers_fichier):
    with open(chemin_vers_fichier, 'r', encoding='utf-8') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        for ligne in reader:
            numero = ligne[0] # à compléter
            mesure = ligne[1]  # à compléter
            maintenant = datetime.now()
            ajouter_mesure(connexion_bd, numero, mesure,maintenant)   # à compléter


def ajouter_mesure(connexion_bd, num_inventaire, date, valeur):
    try:
        cursor = connexion_bd.cursor()
        cursor.execute(f"INSERT into Capteur(numInventaire, refCapteur, typeCapteur) VALUES({num_inventaire},{date}, {valeur})", [])   # à compléter
        connexion_bd.commit()
    except Exception as e:
        print("MySQL [INSERTION ERROR]")
        print(e)


def ecrire_mesures_dans_fichier_csv(connexion_bd, chemin_vers_dossier, numInventaire, date_debut, date_fin):

    print("")
    print(f"Écriture du fichier CSV à partir de la BD: capteur n°{numInventaire} entre {date_debut} et {date_fin}")

    maintenant = datetime.now()
    print(f"Maintenant: " + maintenant.strftime('%d/%m/%Y %H:%M:%S (+%fns)'))

    nom_fichier = "nombres-output_" + str(maintenant.strftime('%Y%m%d%H%M%S'))   
    chemin_vers_fichier = chemin_vers_dossier + nom_fichier

    print(f"Fichier CSV: {chemin_vers_fichier}")

    cursor = connexion_bd.cursor()
    cursor.execute(f"SELECT * FROM Capteurs WHERE numInventaire = {numInventaire} AND DATE<{date_fin} AND DATE >{date_debut}", [])   # à compléter
    with open(chemin_vers_fichier, 'w', encoding='utf-8') as fichier:
        writer = csv.writer(fichier, delimiter=';', quotechar='"')
        for (bim, bam, boum) in cursor:   # à compléter
            writer.writerow([bim, bam, boum])   # à compléter

    print(f"Écriture terminée")


def ecrire_mesures_dans_fichier_json(connexion_bd, chemin_vers_dossier, numInventaire, date_debut, date_fin):

    print("")
    print(f"Écriture du fichier JSON à partir de la BD: capteur n°{numInventaire} entre {date_debut} et {date_fin}")

    maintenant = datetime.now()
    print(f"Maintenant: " + maintenant.strftime('%d/%m/%Y %H:%M:%S (+%fns)'))

    nom_fichier = "nombres-output_" + ""   # à compléter, sans oublier le ".json"
    chemin_vers_fichier = chemin_vers_dossier + nom_fichier

    print(f"Fichier JSON: {chemin_vers_fichier}")

    mesures = []

    cursor = connexion_bd.cursor()
    cursor.execute("...", [])   # à compléter
    with open(chemin_vers_fichier, 'w', encoding='utf-8') as fichier:
        # à compléter / ne pas oublier le formatage des dates, avec strftime('%Y-%m-%d %H:%M:%S'), et des valeurs
        # for (...) in cursor:
        #    mesures.append({'clé1': valeur1, 'clé2': valeur2, ...})

        # indent=4 => permet de mettre en forme le JSON
        # sort_keys=True => permet de trier les clés du dictionnaire (garantie d'avoir toujours les clés dans le même ordre dans le JSON)
        json.dump(mesures, fichier, indent=4)  # , sort_keys=True)

    print(f"Écriture terminée")


# Renvoie le numéro de ligne du script d'où est appelée cette fonction
def line_number():
    return currentframe().f_back.f_lineno


# Programme principal

CHEMIN_INPUT = "./fichiers/input/"
CHEMIN_OUTPUT = "./fichiers/output/"
NOM_FICHIER_MESURES = "mesures-a-lire.csv"


print("")
print(f"Début du Programme principal (ligne {line_number()} du script {__file__})")

print("")
print(f"### Penser à décommenter les lignes suivantes du script (après la ligne {line_number()}) pour tester les fonctions ###")

#lire_fichier_csv(CHEMIN_INPUT + NOM_FICHIER_MESURES)
#ecrire_fichier_csv(CHEMIN_OUTPUT)

bd = ouvrir_connexion_bd()

if bd is not None:
    afficher_liste_capteurs(bd)
    ajouter_mesures_depuis_fichier_csv(bd, CHEMIN_INPUT + NOM_FICHIER_MESURES)
    # ecrire_mesures_dans_fichier_csv(bd, CHEMIN_OUTPUT, 1, "2020-04-30", "2020-05-01")
    # ecrire_mesures_dans_fichier_json(bd, CHEMIN_OUTPUT, 1, "2020-04-30", "2020-05-01")

# fermer_connexion_bd(bd)

print("")
print(f"Fin du Programme principal (ligne {line_number()} du script)")
print("")
