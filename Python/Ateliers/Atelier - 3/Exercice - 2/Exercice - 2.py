# Pascal, Python 3.10 | Développé le 12 Septembre 2022 sous l'IDE Pycharm

def mots_Nlettres(lst_mot:list, n:int) -> list:
    """
    La fonction mots_Nlettres() permet de ranger dans une liste uniquemet les mots contenant n caractères

    :param lst_mot(list): Représente la liste de mots à tester
    :param n(int): Représente la taille des mots à respecter
    :return liste_n(list): La valeur de retour est une liste qui va contenir tous les mots de la liste ayant n caractères
    """

    liste_n = []

    for i in lst_mot:
        if len(str(i)) == n:
            liste_n.append(i)

    return liste_n

def test_function(function:callable, test:int) -> str:
    """
    La fonction test_function() permet de tester divers fonctions

    :param mots_Nlettres(callable): Représente la fonction à tester
    :param test(int): Représente le test à faire
    :return message(str): La valeur de retour est un message permettant de voir la réussite ou non du test
    """
    message = ""

    if test == 1:
        if(len(function) > 0):
            message = "ERROR, la liste doit être vide normalement"
        else:
            message = "SUCCESS, réussite de la fonction sur une liste vide"

    return message

def commence_par(mot:str, prefixe:str) -> bool:
    """
    La fonction commence_par() permet de vérifier que mot commence par prefixe

    :param mot(str): Représente le mot que l'on va tester
    :param prefixe(str): Représente le préfixe qui va être utilisé pour être comparé avec le mot
    :return: La valeur de retour est un booléen qui permet de savoir si le mot commence par prefixe
    """

    mot = mot.capitalize() # Je préfère mettre une majuscule au début du mot et du préfixe pour que le test soit uniforme
    prefixe = prefixe.capitalize()

    return mot[:len(prefixe)] == prefixe

def finit_par(mot:str, suffixe:str) -> bool:
    """
    La fonction finit_par() permet de vérifier que mot finit par suffixe

    :param mot(str): Représente le mot
    :param suffixe(str): Représente le suffixe
    :return: La valeur de retour est un booléen True | False qui représente la présence de suffixe dans mot
    """
    mot = mot.lower()
    suffixe = suffixe.lower()

    return mot[len(mot)-len(suffixe):len(mot)] == suffixe

def finissent_par(lst_mot:list, suffixe:str) -> list:
    """
    La fonction finissent_par() permet de créer une liste avec les mots d'une liste finissant par suffixe

    :param lst_mot(list): Représente la liste de mot qui va être testé
    :param suffixe(str): Représente le suffixe qui va être comparé
    :return liste_retour(list): La valeur de retour est une liste contenant tous les mots ayant pour suffixe, suffixe
    """

    liste_retour = []

    for i in lst_mot:
        if finit_par(i, suffixe):
            liste_retour.append(i)

    return liste_retour

def commencent_par(lst_mot:list, prefixe:str) -> list:
    """
    La fonction commencent_par() permet d'ajouter à une liste les mots qui commencent par prefixe

    :param lst_mot(list): Représente la liste de mots
    :param prefixe(str): Représente le prefixe
    :return liste_retour(list): La valeur de retour est une liste contenant tous les mots ayant pour préfixe prefixe
    """

    liste_retour = []

    for i in lst_mot:
        if commence_par(i, prefixe):
            liste_retour.append(i)

    return liste_retour

def liste_mots(lst_mot:list, prefixe:str, suffixe:str, n:int) -> list:
    """
    La fonction liste_mots() permet de renvoyer une liste de mots ayant uniquement le prefixe, le suffixe et le nombre n de caractères

    :param lst_mot(list): Représente la liste de départ
    :param prefixe(str): Représente le préfixe
    :param suffixe(str): Représente le suffixe
    :param n(int): Représente la longueur des mots à avoir
    :return liste_retour(list): La valeur de retour est une liste contenant tous les mots ayant les prefixe, suffixe et n caractères
    """
    liste_prefixe = commencent_par(lst_mot, prefixe)
    liste_suffixe  = finissent_par(liste_prefixe, suffixe)
    liste_retour = mots_Nlettres(liste_suffixe, n)

    return liste_retour

def dictionnaire(fichier:str) -> None:
    """
    La fonction dictionnaire() permet d'afficher tous les mots présents dans un fichier

    :param fichier(str): Représente le nom du fichier
    :return: Pas de valeur de retour, c'est une procédure
    """
    # ouverture du fichier en lecture (r=read) f=open("profs.txt","r")
    f = open(fichier, "r")
    c = f.readline()  # lecture d'une ligne dans une chaine # de caractères
    print("** Contenu du fichier **")
    while c != "":
        print(c)
        c = f.readline()
    print("** fin **")

if __name__ == '__main__':

    lst_mot = ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir",
               "aimer"]

    # Test sur la liste pour récupérer uniquement les mots de 5 caractères
    print("-----------------------------")
    print(mots_Nlettres(lst_mot, 5))
    print(test_function(mots_Nlettres([], 5), 1)) # Test sur une liste vide
    # Test pour vérifier que bonjour commence bien par bon
    print("-----------------------------")
    print(commence_par("bonjour", "bon"))
    # Test pour vérifier que bonjour finit bien par jour
    print("-----------------------------")
    print(finit_par("bonjour", "jour"))
    # Test ajout des mots ayant pour suffixes oir dans une liste
    print("-----------------------------")
    print(finissent_par(lst_mot, "oir"))
    print(test_function(finissent_par([], "oir"), 1)) # Test de la fonction sur une liste vide
    # Test ajout des mots ayant pour préfixe pou
    print("-----------------------------")
    print(commencent_par(lst_mot, "pou"))
    print(test_function(commencent_par([], "pou"), 1))  # Test de la fonction sur une liste vide
    # Test récupération d'une liste ayant uniquement les mots qui ont pou en prefixe et oir en suffixe
    print("-----------------------------")
    print(liste_mots(lst_mot, "pou", "oir", 7))
    print(test_function(liste_mots([], "pou", "oir", 6), 1)) # Test récupération liste avec une liste vide
    # Test affichage mots présents dans un fichier
    print("-----------------------------")
    print(dictionnaire("littre.txt"))










