from datetime import date

def date_est_valide(jour:int,mois:int,annee:int) -> bool:

    """
    date_est_valide permet de vérifier que le format d'une date est bien valide
    :param jour:
    :param mois:
    :param annee:
    :return:
    Le retour est un booléen True ou False permettant de valider la date
    """
    if(jour <0 or jour >31):

        return(False)

    if(mois < 0 or mois > 12):

        return(False)

    if(annee < 1900 or annee > 2022):

        return(False)

    else:
        return(True)

def saisie_date_naissance() -> date:
    """
    La fonction permet de renvoyer une date au format correct
    :return:
    La valeur de retour est une date
    """
    jour = input("Jour de naissance au format J : ")
    mois = input("Mois de naissance au format M : ")
    annee = int(input("Annee au format AAAA : "))

    if(jour[0] == "0"):
        jour = int(jour[1])
    if(mois[0] =="0"):
        mois = int(mois[1])

    return (date(annee, mois, jour))

def age(date_naissance:date) -> int:
    """
    la fonction age() permet de renvoyer l'âge de l'utilisateur en fonction de sa date de naissance
    :param date_naissance:
    :return:
    La valeur de retour est un entier représentant l'âge
    """
    today = date.today().year

    return (today - date_naissance.year)

def est_majeur(date_naissance:date) -> bool:
    """
    La fonction est_majeur() permet de savoir si un utilisateur est majeur
    :param date_naissance:
    :return:
    La valeur de retour est True ou False
    """
    if(age(date_naissance) >= 18):
        return True
    else:
        return False

def enjoy_access():
    """
    la foncion enjoy_access() vérifie l'accès d'un utilisateur à la boite
    :return:
    La valeur de retour est un message comprenant différentes informations sur l'utilisateur
    """
    date_naissance = saisie_date_naissance()
    a = age(date_naissance)

    #print(date_naissance.day)
    #print(date_naissance.month)
    #print(date_naissance.year)

    if(date_est_valide(date_naissance.day, date_naissance.month, date_naissance.year) == False):
        print("La date de naissance saisie n'est pas valide. Merci de renouveler l'opération.")
        enjoy_access()

    else:

        if(est_majeur(date_naissance)):
            print(f"Bienvenu vous êtes née le {date_naissance.strftime('%d/%m/%Y')}\n Vous avez {a} ans\n L'accès est donc autorisé !")
        else:
            print(f"Bienvenu vous êtes née le {date_naissance.strftime('%d/%m/%Y')}\n Vous avez {a} ans\n L'accès n'est donc pas autorisé !")




#print(est_majeur(date(2007,4,29)))
if __name__ == '__main__':
    enjoy_access()

