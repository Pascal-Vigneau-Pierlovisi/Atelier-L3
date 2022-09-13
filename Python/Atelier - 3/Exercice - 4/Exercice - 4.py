# Pascal, Python 3.10 | Développé le 13 Septembre 2022 sous l'IDE Pycharm

def mot_correspond(mot: str, motif: str) -> bool:
    """
    La fonction mot_correspond() permet de déterminer si le mot pourrait correspondre au motif

    :param mot(str): Représente le mot que l'utilisateur à rentré
    :param motif(str): Représente le motif
    :return correspond(bool): Le retour de la fonction est un booléen qui permet de savoir si le mot pourrais être le motif
    """
    correspond = False
    close = True
    i = 0

    if len(mot) == len(motif):
        while i < len(mot) and close:
            if mot[i] == motif[i]:
                correspond = True
            if motif[i] != "." and mot[i] != motif[i]:
                correspond = False
                close = False
            i += 1

    return correspond


def presente(lettre: str, mot: str) -> list:
    """
    La fonction presente() permet de savoir si lettre est présente dans mot

    :param lettre(str): Représente la lettre recherchée dans le mot
    :param mot(str): Représente le mot où on cherche la lettre dedans
    :return valeur_retour(list): La valeur de retour est une liste qui est vide si la lettre n'est pas trouvé
     et elle contient les indexs de la lettre si la lettre est trouvé
    """
    valeur_retour = []

    if len(lettre) == 1:
        for i in range(len(mot)):
            if mot[i] == lettre:
                valeur_retour.append(i)

    return valeur_retour


def mot_possible(mot: str, lettres: str):
    """
    La fonction mot_possible() permet de savoir si avec les différentes lettres, on peut faire le mot

    :param mot(str): Représente le mot que l'utilisateur voudrait faire
    :param lettres(str): Représente les lettres qui sont en possession de l'utilisateur
    :return possible(bool): La valeur de retour est un booléen qui permet de savoir c'est avec les lettres l'utilisateur
    peut faire le mot qu'il souhaite faire
    """
    possible = False

    tab = []

    for i in range(len(lettres)):
        value = presente(lettres[i], mot)
        for n in value:
            if n not in tab:
                tab.append(n)

    if len(tab) == len(mot):
        possible = True

    return possible


def mots_Nlettres(lst_mot: list, n: int) -> list:
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


def build_list(fileName: str) -> list:
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


def mot_optimaux(dico: list, lettres: str) -> list:
    """
    La fonction mot_optimaux() permet de renvoyer une liste contenant les mots avec la longueur max que l'on peut faire
    avec les lettres.

    :param dico(list): Représente la liste des mots que l'utilisateur souhaite faire
    :param lettres(str): Représente les lettres auquelles l'utilisateur à accès
    :return: La valeur de retour est une liste contenant les mots ayant le plus grand nombre de caractères
    que l'utilisateur peut faire
    """

    return mots_Nlettres(dico, len(lettres))


if __name__ == '__main__':
    # Test de la fonction mot_correspond()
    print("----------------------")
    print(mot_correspond("pascal", "p....l"))  # Test n°1
    print(mot_correspond("pascal", "pd..al"))  # Test n°2
    # Test de la fonction presente()
    print("----------------------")
    print(presente("a", "pascal"))  # Test n°1
    print(presente("pa", "pascal"))  # Test n°2
    # Test de la fonction mot_possible()
    print("----------------------")
    print(mot_possible("pascal", "mnpgalskcjarl"))  # Test n°1
    # Test de la fonction mot_optimaux()
    liste = build_list("capitales_pays.txt")
    print(mot_optimaux(liste, "abcdefg"))  # Test de la création d'une liste optimale
