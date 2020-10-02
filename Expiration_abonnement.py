'''
##############################################################################################
#                                                                                            #
#                           Memphis 95, Secret's Rezal, KIN 219                              #
#                                                                                            #
##############################################################################################'''


# Pour installer mysql-connector: pip install mysql-connector

import mysql.connector

mydb = mysql.connector.connect(
    host="172.20.0.3",
    user="root",
    passwd="rezal@K1N",
)

cursor = mydb.cursor()


def modifier_une_entree(nouvelle_valeur, cle_id):  # permet de modifier des infos sur une entrée
    sql = "UPDATE intra.auth_user SET expiry_date = %s WHERE id = %s"
    val = (nouvelle_valeur, cle_id)
    cursor.execute(sql, val)
    mydb.commit()
    return()


print("Programme de modification/ajout des expirations d'abonnements\n")

exit_condition = False

while not exit_condition:

    nom = input("Nom: ")
    prenom = input("Prenom: ")

    sql = "SELECT user_ptr_id,expiry_date FROM intra.users_client uc JOIN intra.auth_user ON intra.auth_user.id=user_ptr_id WHERE nom= %s AND prenom = %s"
    val = (nom, prenom)
    cursor.execute(sql, val)
    records = cursor.fetchall()
    L = []
    for row in records:
        L.append((row[0], row[1]))
    if len(L) > 1:
        print("Utilisateur présent 2 fois dans la BDD, veuillez en supprimer un avant toute modification")
    elif len(L) == 0:
        print("Utilisateur introuvable..., veuillez vérifier que ce dernier existe bien dans la BDD (l'orthographe est peut-être différent)")
    else:
        p = "Date d'expiration actuelle de l'utilisateur: " + str(L[0][1])+"\n"
        print(p)
        a = 0
        while a == 0:
            test = input(
                "Saisir une nouvelle date d'expiration pour l'utilisateur? (Y pour oui/N pour non) ")
            a = 1
            if test == "Y":
                date_expiration = input("Nouvelle date d'expiration? (format AAAA-MM-DD) ")
                modifier_une_entree(date_expiration, L[0][0])
                print("Mofification effectuée!")
            elif test == "N":
                print("Pas de modification effectuée!")
            else:
                a = 0
    print("")
    while True:
        condition = input("Veut tu changer un autre abonnement ? (Y pour oui/N pour non) :")
        if condition == "Y":
            break
        elif condition == "N":
            exit_condition = True
            break
        
mydb.close()
