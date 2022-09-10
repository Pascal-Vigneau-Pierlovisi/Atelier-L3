# Pascal, Python 3.10 | Développé le 8 Septembre 2022 sous l'IDE Pycharm
from math import ceil


def position(L:list,e:int)->int:
    """
    La fonction position permet de regarder la position dans la liste L dans entier e

    :param L(list): Représente une liste d'entiers
    :param e(int): Représente un entier
    :return is_present(int): La valeur de retour est un entier qui sera soit -1 si le nombre n'est pas présent soit 1
    si le nombre 1 est présent dans la liste
    """
    is_present = -1
    height = len(L) -1

    """
    for i in L:
        if i == e:
            is_present = 1
    """
    while height != -1:
        if liste[height] == e:
            is_present = 1
        height-=1

    return is_present

def nb_occurrences(L:list,e:int)->int:
    """
    La fonction nb_occurence() permet de savoir le nombre d'occurence de l'entier e dans la liste L

    :param L(list): Représente une liste de nombre entiers
    :param e(int): Représente un entier
    :return occurence(int): La valeur de retour est un int représentant le nombre d'occurence de e dans la L
    """
    occurence = 0

    for i in L:
        if i == e:
            occurence +=1

    return occurence

def est_triee(L:list)->bool:
    """
    La fonction est_triee() permet de vérifier que les éléments de la liste L sont bien rangés dans l'ordre croissant

    :param L(list): Représente une liste d'entiers
    :return trie(bool): La valeur de retour est un booléen True / False qui représente si la liste est bien rangé
    """
    trie = True  # Valeur de retour initialisé par défaut sur True
    temp = L[0] # Premier élément à vérifier dans la liste pour la boucle for
    i = 1
    max = len(L)

    print(temp)

    while i < max and trie:

        if temp < L[i]:
            temp = L[i]

        else :
            trie = False

        i = i +1

    """
    for i in range(1, len(L) -1):
        if temp < L[i]:
            temp = L[i]
        else:
            trie = False
    """


    return trie

def sorted(L:list)->list:
    """
    La fonction sorted permet de renvoyer une liste L triée

    :param L(list): Représente une liste de nombres entiers
    :return liste_retour(list): La valeur de retour est une liste d'entiers triée et rangé par ordre croissant
    """
    liste_retour = []

    if(est_triee(L)):

        liste_retour = L

    else:
        while L: # tant que la liste n'est pas vide
            mini = L[0] # On initialise la valeur qui va être comparé par le premier élément de la liste
            for i in L: # Parcours des éléments de la liste L
                if i < mini: # Cette structure conditionnelle permet de trouver l'élément le plus petit de la liste
                    mini = i
            L.remove(mini)
            liste_retour.append(mini)

    return liste_retour

def searchItem(L:list, e:float)->bool:
    """
    La fonction searchItem() permet de vérifier si l'élément e est présent dans la liste L

    :param L(list): Représente la liste
    :param e(float): Représente l'entier à rechercher dans la liste L
    :return trouve(bool): La valeur de retour est un booleen True | False en fonction de la présence de e dans L
    """
    trouve = False
    start = 0
    end = len(L) - 1
    mil = 0

    while trouve != True and start <= end:
        mil = ceil((start + end) /2)
        if L[mil] == e:
            trouve = True
        else:
            if e > L[mil]:
                start = mil + 1
            else:
                end = mil - 1
    if trouve == True:
        print("La valeur ", e , " est au rang ", mil)
    else:
        print("La valeur ", e , " n'est pas dans le tableau")

    return trouve

def a_repetitions(L:list)->bool:
    """
    La fonction a_repetitions() permet de savoir le nombre de répétitions d'un élément dans la liste L

    :param L(list): Représente la liste à vérifier
    :return repet(bool): La valeur de retour est un booléen True | False en fonction de si une répétition est trouvé
    """
    repet = True
    t = []
    i = 0
    max = len(L) - 1


    while L and repet and i < max :


        if L[i] in t:
            repet = False
        else:
            t.append(L[i])
        i+=1


    return repet

if __name__ == '__main__':
    #Test savoir si 18 est présent dans liste
    liste = [10, 20, 89, 11]
    print(position(liste, 18))
    # Test savoir si 10 est présent dans liste
    print(position(liste, 10))
    # Test savoir le nombre d'occurence de 10 dans liste
    liste = [10, 20, 89, 11]
    print(f"le nombre 10 est présent {nb_occurrences(liste, 10)} fois dans la liste")
    # Test savoir si liste est bien rangé
    print(est_triee(liste))
    print("------------------------------------")
    value = [10, 20, 89, 111, 1021]
    print(est_triee(value))
    print("------------------------------------")
    new_liste = sorted(liste)
    print(new_liste)
    print("------------------------------------")
    # Test pour trouver un élément e dans la liste new_liste
    searchItem(new_liste, 99)
    # Test pour savoir le nombre de répétitions d'un élément dans la liste new_liste
    print(a_repetitions(new_liste))





