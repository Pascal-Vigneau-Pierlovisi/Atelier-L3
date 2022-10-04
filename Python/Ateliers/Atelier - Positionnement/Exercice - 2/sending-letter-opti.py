#Pascal, 3.10 | Developpé sous l'IDE Pycharm le 8 Septembre 2022 | Le code n'est pas finit

# Liste de lieu de livraison zone OM1
OM1 = ["Guyane", "Guadeloupe", "Martinique", "La Réunion", "St Pierre et Miquelon", "St Barthélémy",
       "St-Martin et Mayotte"]

# Liste de lieu de livraison zone OM2
OM2 = ["Nouvelle-Calédonie", "Polynésie française", "Wallis-et-Futuna", "T.A.A.F"]

# Dictionnaire contenant les différents types de lettre et permettant de faire un lien avec
LETTER = {
    "Lettre Verte" : [[20.0, 100.0, 250.0, 500.0, 1000.0, 3000.0],[1.16, 2.32, 4.00, 6.00, 7.50, 10.50], [0.5, 0.11]],
    "Lettre Prioritaire" : [[20.0, 100.0, 250.0, 500.0, 3000.0],[1.43, 2.86, 5.26, 7.89, 11.44], [0.5, 0.11]],
    "Ecopli" : [[20.0, 100.0, 250.0],[1.14, 2.28, 3.92], [0.02, 0.05]]
}

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

def returnIndexPrice(letter:str, weight:float) ->int:
    """
    La foncton returnPrice() permet de retourner l'index du prix de la lettre en fonction de son poids
    :param letter: le type de lettre que l'utilisateur a saisie
    :param weight: le poids de la lettre que l'utilisateur a saisie
    :return: La valeur de retour est un int qui représente l'index du prix
    """
    index = len(LETTER[letter][0]) - 1

    for key, value in LETTER.items():

        if(letter == key):

            for i in range(0, index):

                if weight < LETTER[user_letter][0][index]:

                    index-=1

        #print("KEY : ", key, " Value : ", value)

    print(f"DEBUG : {index}")

    return index




def checkWeight(weight:float, letter:str) ->bool:
    """
    La fonction checkWeight() permet de vérifier que le poids saisi est > 0
    :param weight: poids de la lettre
    :return: la valeur de retour est un booléen
    """

    max_weight = len(LETTER[letter][0]) -1

    print("DEBUG : ", max_weight)

    if weight < 0 or weight > LETTER[letter][0][max_weight]:
        return False

    else:
        return True

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

    print(f"Voici les différents tarifs pour {user_letter} : ")
    print("-----------------------------------------")

    for i in range(0, len(LETTER[user_letter][0])):
        print(f"Jusqu'à {LETTER[user_letter][0][i]} grammes ---> {LETTER[user_letter][1][i]} euros")

    letter_weight = 0

    try:

        letter_weight = float(
            input(("-----------------------------------------\nMerci de rentrer le poids de votre lettre : ")))

    except:
        print(
            "Une erreur est survenue lors de la saisie du poids de la lettre, merci de renouveler l'opération de saisie !")
        quit()

    if (checkWeight(letter_weight, user_letter) == False):
        print("Le poids saisi est interdit !")
        quit()

    print(f"Merci de choisir la destination de votre {user_letter} : ")

    print("------------------ZONE OM1-----------------------")

    for om1 in OM1:
        print(f"- {om1}")

    print(
        f"\n Zone OM1 supplément de {LETTER[user_letter][2][0]} centimes par tranche de 10 g supplémentaire")

    print("------------------ZONE OM2-----------------------")

    for om2 in OM2:
        print(f"- {om2}")

    print(
        f"\n Zone OM2 supplément de {LETTER[user_letter][2][1]} centimes par tranche de 10 g supplémentaire")
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

    print(index)