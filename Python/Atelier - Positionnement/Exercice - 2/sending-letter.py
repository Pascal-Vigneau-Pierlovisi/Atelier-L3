# Liste de lieu de livraison zone OM1
OM1 = ["Guyane", "Guadeloupe", "Martinique", "La Réunion", "St Pierre et Miquelon", "St Barthélémy", "St-Martin et Mayotte"]

# Liste de lieu de livraison zone OM2
OM2 = ["Nouvelle-Calédonie", "Polynésie française", "Wallis-et-Futuna", "T.A.A.F"]

# Dictionnaire des différents prix de la Lettre Verte en fonction des poids

LV = {
    20.0 : 1.16,
    100 : 2.32,
    250 : 4.00,
    500 : 6.00,
    1000 : 7.50,
    3000 : 10.50
}

LP = {
    20.0 : 1.43,
    100 : 2.86,
    250 : 5.26,
    500 : 7.89,
    3000 : 11.44
}

ECO = {
    20.0 : 1.14,
    100 : 2.28,
    250 : 3.92,
}

# Dictionnaire contenant les différents types de lettre et permettant de faire un lien avec
LETTER = {
    "Lettre Verte" : LV,
    "Lettre Prioritaire" : LP,
    "Ecopli" : ECO
}

# Liste des prix qui va se remplir avec les prix adéquates en fonction de la lettre
liste_prix = []

# Liste des poids ayant la même taille que la liste liste_prix et se remplissant avec les poids liés au prix
liste_poids = []

def letterIsCorrect(letter:str) ->bool:

    """
    La fonction letterIsCorrect() permet de vérifier que le type de lettre choisi par l'utilisateur est bien correct
    :param letter:  Représente le type de lettre choisi par l'utilisateur
    :return: La valeur de retour de cette fonction est un booléen True ou False
    """

    if(letter in LETTER):
        return True

    else:
        return False

def addList(letter:str) ->bool:

    """
    La fonction addList permet de remplir les différentes listes contenant les poids et prix en fonction du type de lettre
    :param letter: Représente le type de lettre
    :return: La valeur de retour est un booleén
    """

    if letterIsCorrect(letter):

        for key, value in LETTER[letter].items():

            liste_prix.append(value)
            liste_poids.append(key)

        return True

    else:

        return False

def returnPriceDest(letter:str, dest:str, weight:float) ->float:
    """
    La fonction ReturnPriceDest() permet de renvoyer le prix des suppléments d'une lettre en fonction de sa destination et de son poids
    :param letter: le type de lettre que l'utilisateur a choisi
    :param dest: le lieu de destination que l'utilisateur a choisi
    :return: la valeur de retour est un entier
    """

    if letter == "Lettre Verte" or letter == "Lettre Prioritaire":

        if dest in OM1:


            return 0.05 * weight

        else:

            return 0.11 * weight

    if letter == "Ecopli":

        if dest in OM1:

            return 0.02 * weight

        else:

            return 0.05 * weight

def returnIndexPrice(letter:str, weight:float) ->int:
    """
    La foncton returnPrice() permet de retourner l'index du prix de la lettre en fonction de son poids
    :param letter: le type de lettre que l'utilisateur a saisie
    :param weight: le poids de la lettre que l'utilisateur a saisie
    :return: La valeur de retour est un int qui représente l'index du prix
    """

    if(weight < liste_poids[0]):

        return 0

    else:

        index = len(liste_prix) - 1

        for i in range(0, len(liste_prix)):

            if weight < liste_poids[index]:
                index-=1

            if index == -1:
                index = 0

        if index == len(liste_prix)-1:
            return index

        else:
            return index + 1

def choiceDest(dest:str) ->bool:
    """
    La fonction choiceDest() permet de vérifier si la destination choisie existe bien.
    :param dest: Représente la destination saisie par l'utilisateur
    :return: La valeur de retour est un booléen True ou False
    """

    if dest in OM1 or dest in OM2:
        return True

    else:
        return False

def checkWeight(weight:float) ->bool:
    """
    La fonction checkWeight() permet de vérifier que le poids saisi est > 0
    :param weight: poids de la lettre
    :return: la valeur de retour est un booléen
    """

    if weight < 0:
        return False

    else:
        return True

if __name__ == '__main__':

    try_user = 0

    print("Bonjour, merci de mettre le type de lettre que vous souhaitez utiliser : ")

    for i in LETTER:
        print(f"- {i}")

    user_letter = ""

    while letterIsCorrect(user_letter) == False:


        if try_user == 3:

            print("Nombre d'essais limite atteint ! veuillez renouveler l'opération.")
            quit()

        else:
            user_letter = str(input("Votre choix : "))
            try_user += 1

    try_user = 0

    if addList(user_letter) == False:

        print("Une erreur est survenue merci de bien vouloir renouveler l'opération")
        quit()

    print(f"Voici les différents tarifs pour {user_letter} : ")
    print("-----------------------------------------")

    for i in range(0, len(liste_prix)):
        print(f"Jusqu'à {liste_poids[i]} grammes ---> {liste_prix[i]} euros")

    letter_weight = 0

    try:

        letter_weight = float(input(("-----------------------------------------\nMerci de rentrer le poids de votre lettre : ")))

    except:
        print("Une erreur est survenue lors de la saisie du poids de la lettre, merci de renouveler l'opération de saisie !")
        quit()

    if(checkWeight(letter_weight) == False):
        print("Le poids saisi est négatif, cela est interdit !")
        quit()


    print(f"Merci de choisir la destination de votre {user_letter} : ")

    print("------------------ZONE OM1-----------------------")

    for om1 in OM1:
        print(f"- {om1}")

    print(f"\n Zone OM1 supplément de {returnPriceDest(user_letter, 'Guyane', 1)} centimes par tranche de 10 g supplémentaire")

    print("------------------ZONE OM2-----------------------")

    for om2 in OM2:
        print(f"- {om2}")

    print(f"\n Zone OM2 supplément de {returnPriceDest(user_letter, 'Nouvelle-Calédonie', 1)} centimes par tranche de 10 g supplémentaire")
    print("-------------------------------------------------")

    user_dest = ""

    while choiceDest(user_dest) == False:

        if try_user == 3:

            print("Nombre d'essais limite atteint ! veuillez renouveler l'opération.")
            quit()

        else:
            user_dest = str(input("Votre choix : "))
            try_user += 1

    index = returnIndexPrice(user_letter, letter_weight)

    if(index != 0):
        extra_weight = letter_weight - liste_poids[index - 1]
        print(f"Le prix de la lettre est de : {liste_prix[index] + returnPriceDest(user_letter, user_dest, extra_weight)}")


    else:
        print(
            f"Le prix de la lettre est de : {liste_prix[index]}")













