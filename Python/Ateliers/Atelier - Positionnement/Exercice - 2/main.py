OM1 = ["Guyane", "Guadeloupe", "Martinique", "La Réunion", "St Pierre et Miquelon", "St Barthélémy", "St-Martin et Mayotte" ]
OM2 = ["Nouvelle-Calédonie", "Polynésie française", "Wallis-et-Futuna", "T.A.A.F"]

choix_lettre = {
    "LETTRE VERTE" : "LV",
    "LETTRE PRIORITAIRE" : "LP",
    "ECOPLI" : "EP"
}

sticker = 0.50

def choixLettre(choice:str) -> bool:
    """
    La fonction choixLettre() permet de vérifier que l'utilisateur à bien choisi une lettre existante
    :param choice:
    :return:
    La valeur de sortie est un booléen
    """

    if(choice.upper() not in choix_lettre):
        print("La lettre n'existe pas !")
        return False
    else:
        #print("DEBUG")
        return True


def choixAdresse(destination : str) -> int:

    """
    LA fonction choixAdresse() permet de faire une vérification sur le lieu de livraison choisi par l'utilisateur
    :param destination:
    :return: La valeur de retour est un entier représentant à quelle liste appartient le lieu de destination
    """

    for i in OM1:
        if destination == i:
            return 1
    for b in OM2:
        if destination == b:
            return 2

def reglement(poids : float, lettre : str, destination : int) -> float:
    """
    La fonction reglement() permet de calculer le prix de la lettre en fonction du poids du type de lettre et de la destination
    :param poids: poids de la lettre
    :param lettre: type de la lettre
    :param destination: lieu de destination de la lettre
    :return: la valeur de retour est un float représentant le prix de la lettre
    """

    price = 0
    poids_supp = 0

    print("DEBUG")

    if(lettre == "LETTRE VERTE"):
        if poids < 20:
            price = 1.16
        if poids > 20 and poids < 100:
            price = 2.32
            poids_supp = poids - 20
        if poids > 100 and poids < 250:
            price = 4.00
            poids_supp = poids - 100
        if poids > 250 and poids < 500:
            price = 6.00
            poids_supp = poids - 250
        if poids > 500 < 1000:
            price = 7.50
            poids_supp = poids - 500
        if poids > 1000 and poids < 3000:
            price = 10.50
            poids_supp = poids - 1000
        if(destination == 1):
            price = ((poids_supp * 0.05)/10) + price
        if(destination ==2):
            price = ((poids_supp * 0.11)/10) + price

        return price

    if(lettre == "LETTRE PRIORITAIRE"):
        if poids < 20:
            price = 1.43
        if poids > 20 and poids < 100:
            price = 2.86
            poids_supp = poids - 20
        if poids > 100 and poids < 250:
            price = 5.26
            poids_supp = poids - 100
        if poids > 250 and poids < 500:
            price = 7.89
            poids_supp = poids - 250
        if poids > 500 and poids< 3000:
            price = 11.44
            poids_supp = poids - 500


        if(destination == 1):
            price = ((poids_supp * 0.05)/10) + price
        if(destination ==2):
            price = ((poids_supp * 0.11)/10) + price

        return price

    if (lettre == "ECOPLI"):
        if poids < 20:
            price = 1.14
        if poids > 20 and poids < 100:
            price = 2.28
            poids_supp = poids - 20
        if poids > 100 and poids < 250:
            price = 3.92
            poids_supp = poids - 100

        if (destination == 1):
            price = ((poids_supp * 0.02) / 10) + price
        if (destination == 2):
            price = ((poids_supp * 0.05) / 10) + price

        return price







def main():
    ###############CHOIX DE LA LETTRE#####################
    print("Bonjour, merci de choisir la lettre que vous souhaitez envoyer : ")
    for i in choix_lettre:
        print("-", i)
    choice = input("Votre choix : ")
    if choixLettre(choice) == False:
        main()
    ##############CHOIX DU LIEU###########################
    valid_adress = 0
    choice_lieu = ""

    print("Lieu de livraison disponible : ")
    for b in OM1:
        print("-", b)
    for c in OM2:
        print("-", c)
    while(valid_adress == 0):
        choice_lieu = input("Votre choix : ")
        print("DEBUG : ", choixAdresse(choice_lieu))
        if(choixAdresse(choice_lieu) == 1 or choixAdresse(choice_lieu) == 2):
            valid_adress = 1
        else:
            print("Adresse inconnue, merci de réessayer : ")

    poids = float(input("Poids de la lettre en gramme : "))
    print(f"La lettre est une lettre {choice}, vous souhaitez vous faire livrer en {choice_lieu}\n La livraison sera facturé : {reglement(poids, choice, choixAdresse(choice_lieu))}")








if __name__ == '__main__':
    main()