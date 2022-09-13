# Pascal, Python 3.10 | Développé le 13 Septembre 2022 sous l'IDE Pycharm
import random

def places_lettre(ch : str, mot : str) -> list:
    """
    La fonction places_lettre() permet de renvoyer une liste contenant les index de ch dans mot

    :param ch(str): Représente le caractère à chercher
    :param mot(str): Représente le mot
    :return liste_index(list): La valeur de retour est une liste contenant les index de ch dans mot
    """
    chaine = []

    if(len(ch) != 1):
        print("ch ne doit pas comporter + d'un caractère")

    else:
        for i in range(len(mot)):
            if mot[i] == ch:
                chaine.append(i)

    return chaine

def outputStr(mot:str, lpos:list) -> str:
    """
    La fonction outputStr() permet de voir l'avancement du pendu

    :param mot(str): Représente le mot à trouver
    :param lpos(list): Représente la liste des index trouvés
    :return chaine(str): La valeur de retour est le mot avec les lettres trouvées
    """

    chaine = ""
    tab = ["_"] * len(mot)

    if(len(lpos) > 0):
        for i in lpos:
            tab[i] = mot[i]

    for i in tab:
        chaine = chaine + i

    return chaine

def build_list(fileName : str) -> list:
    """
    La fonction build_list() permet de générer une liste de mot à l'aide d'un fichier texte

    :param fileName(str): Représente le nom du fichier
    :return liste(list): La valeur de retour est une liste contenant les éléments du fichier texte
    """
    liste = []

    file = open(fileName, "r")
    content = file.readline()
    while content != "":
        value = content.strip("\n")
        value = value.lower()

        liste.append(value)

        content = file.readline()
    file.close()
    return liste

def build_dict(lst: list) -> dict:
    """
    La fonction build_dict() permet de créer un dictionnaire avec des listes de mots en fonction de leurs longueurs

    :param lst(list): Représente la liste de mots à classer
    :return dictionnaire(dict): La valeur de retour est un dictionnaire contenant des listes de mots en fonction de leurs longueurs
    """

    facile = []
    normal = []
    hard = []

    dictionnaire = {
        1 : facile,
        2 : normal,
        3 : hard
    }

    for i in lst:
        if len(i) < 7:
            facile.append(i)
        elif 6 < len(i) < 9:
            normal.append(i)
        else:
            hard.append(i)

    return dictionnaire

def select_word(sorted_words:dict, word_len:int)->str:
    """
    La fonction select_word() permet de séléctionner un mot aléatoirement en fonction de sa longueur

    :param sorted_words(dict): Représente le dictionnaire avec les différentes difficultés
    :param word_len:  Représente la longueur du mot voulue par l'utilisateur
    :return word(str): La valeur de retour est le mot tiré au hasard dans le dictionnaire en fonction de la difficulté
    """
    if word_len < 7:
        word = random.choice(sorted_words[1])

    elif 6 < word_len < 9:
        word = random.choice(sorted_words[2])

    else:
        word = random.choice(sorted_words[3])

    return word

def runGame() -> None:
    """
    La procédure runGame() permet de lancer le jeu
    :return: Aucune valeur de retour c'est une prodédure qui permet le lancement du jeu
    """
    liste_mot_possible = build_list("capitales_pays.txt") # Création de la premiere liste sans niveau
    liste_mot_possible = build_dict(liste_mot_possible) # Trie des mots en fonction de la difficulté
    difficulty = int(input("Merci de mettre la longueur de mot que vous voulez : \n-niveau easy taille du mot < 7\n-niveau normal 6 < taille du mot < 9\n-niveau hard taille du mot > 8\nVotre choix : "))
    mot_a_trouver = select_word(liste_mot_possible, difficulty)
    mot_utilisateur = outputStr(mot_a_trouver, [])
    erreur = 0
    coups = 5
    tableau_lettre_trouve = []
    while mot_utilisateur != mot_a_trouver and erreur != 5:
        choix_user = input("Lettre choisie : ")
        tableau_lettre_trouve += places_lettre(choix_user, mot_a_trouver)
        print(outputStr(mot_a_trouver, tableau_lettre_trouve))
        mot_utilisateur = outputStr(mot_a_trouver, tableau_lettre_trouve)


        if len(places_lettre(choix_user, mot_a_trouver)) == 0:
            erreur +=1
            coups -=1

        if mot_utilisateur == mot_a_trouver:
            print(f"Félicitation le mot à trouver était : {mot_a_trouver}. Vous l'avez trouvé avec {erreur} erreurs")

        print(f"Il vous reste {coups} coups")

        if erreur == 5 :
            print(f"Vous avez perdu désolé :c | le mot à trouver était : {mot_a_trouver}")

        match erreur:
            case 1:
                print("|---] ")
                print("|   ")
                print("|   ")
                print("|   ")
                print("|______")
            case 2:
                print("|---] ")
                print("| O ")
                print("|   ")
                print("|   ")
                print("|______")
            case 3:
                print("|---] ")
                print("| O ")
                print("| T ")
                print("|   ")
                print("|______")
            case 4:
                print("|---] ")
                print("| O ")
                print("| T ")
                print("|/  ")
                print("|______")
            case 5:
                print("|---] ")
                print("| O ")
                print("| T ")
                print("|/ \ ")
                print("|______")

if __name__ == '__main__':

    runGame()






