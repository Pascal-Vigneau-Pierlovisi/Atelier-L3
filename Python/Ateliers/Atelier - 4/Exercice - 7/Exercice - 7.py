# Pascal, Python 3.10 | Développé le 19 Septembre 2022 sous l'IDE Pycharm
import copy
from random import randint


def trie_stupide(lst: list) -> list:
    """
    La fonction trie_stupide permet de trier une liste de manière aléatoire

    :param lst(list): Représente la liste à trier
    :return return_lst(list): La valeur de retour est une liste triée avec de la chance
    """

    return_lst = [""] * len(lst)

    while return_lst != sorted(lst):
        index_1 = randint(0, len(lst) - 1)
        index_2 = randint(0, len(lst) - 1)
        return_lst[index_1] = lst[index_2]

    return return_lst


def trie_insertion(lst: list, n: int) -> list:
    """
    la fonction trie_insertion() permet de trier une liste

    :param lst(list): Représente la liste à trier
    :param n(int): Représente la taille de la liste
    :return lst(list): La valeur de retour est la liste elle-même passée en paramètre mais triée
    """

    for i in range(1, n):
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1] > x:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = x

    return lst


def insertion_sort(lst: list) -> list:
    """
    La fonction insertion_sort() permet de trier une liste

    :param lst(list): Représente la liste
    :return return_lst(list): La valeur de retour est une liste qui représente lst triée
    """

    return_lst = copy.deepcopy(lst)

    for i in range(1, len(return_lst)):
        x = return_lst[i]
        j = i
        while j > 0 and return_lst[j - 1] > x:
            return_lst[j] = return_lst[j - 1]
            j = j - 1
        return_lst[j] = x

    return return_lst


def selection_sort(lst: list) -> list:
    """
    La fonction selection_sort() permet de trier lst

    :param lst(list): Représente la liste à trier
    :return lst(list): La valeur de retour est la liste de départ triée
    """
    n = len(lst)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if lst[j] < lst[min]:
                min = j
        temp_min = lst[min]
        temp_i = lst[i]
        if min != i:
            lst[min] = temp_i
            lst[i] = temp_min

    return lst


def buble_sort(lst: list) -> list:
    """
    La fonction buble_sort() permet de trier la liste lst

    :param lst(list): Représente la liste à trier
    :return lst(list): La valeur de retour est la liste de départ triée
    """

    lst_trie = copy.deepcopy(lst)

    for i in range(len(lst_trie), 1, -1):
        tableau_trie = True
        for j in range(0, i - 1):
            tempj = lst_trie[j]
            tempj1 = lst_trie[j + 1]
            if lst_trie[j + 1] < lst_trie[j]:
                lst_trie[j + 1] = tempj
                lst_trie[j] = tempj1
                tableau_trie = False
        if tableau_trie:
            return lst_trie


def trie_fusion(lst: list) -> list:
    """
    la fonction trie_fusion() permet de retourner une liste triée à partir de la fusion de la division de cette liste

    :param lst(list): Représente la liste à trier
    :return copy_lst(lst): La valeur de retour est une liste triée
    """
    copy_lst = copy.deepcopy(lst)

    if len(copy_lst) <= 1:
        return copy_lst

    else:
        copy_lstA = copy_lst[:len(copy_lst) // 2]
        copy_lstB = copy_lst[(len(copy_lst) // 2):]

        return fusion(trie_fusion(copy_lstA), trie_fusion(copy_lstB))


def fusion(lstA: list, lstB: list) -> list:
    """
    La fonction fusion() permet de renvoyer la fusion de 2 listes triées

    :param lstA(list): Représente la première liste
    :param lstB(list): Représente la deuxième liste
    :return: La valeur de retour est une liste qui représente la fusion des 2 listes
    """

    if len(lstA) == 0:
        return lstB

    if len(lstB) == 0:
        return lstA

    if lstA[0] <= lstB[0]:
        return [lstA[0]] + fusion(lstA[1:], lstB)

    else:
        return [lstB[0]] + fusion(lstA, lstB[1:])

def flat(lst: list) -> list:
    """
    La fonction flat() permet de transformer une liste de liste en une simple liste

    :param lst(list): Représente la liste à transformer
    :return return_lst(list): Représente la liste de retour
    """

    return_lst = []

    for i in range(len(lst)):
        if len(lst[i]) != 0:
            for b in lst[i]:
                return_lst.append(b)

    return return_lst

def radix(lst: list) -> list:
    """
    La fonction radix() permet de trier lst par base c-a-d par rapport au nombre de digits présent dans les éléments

    :param lst(list): Représente la liste à trier
    :return return_lst(list): La valeur de retour est une liste triée
    """
    return_lst = lst.copy()

    m = 0  # Nombre de digits initialisées à 0

    for i in lst:
        m = max(m, i)

    m = len(str(m))  # Permet de savoir le nombre de digits

    for digit in range(0, m):
        tab_number = [[] for i in range(10)]
        for item in return_lst:
            num = item // 10 ** digit % 10  # Permet de récupérer le chiffre souhaité
            tab_number[num].append(item)  # On ajoute dans le tableau les éléments par rapport au chiffre qui
            # représente l'index

        return_lst = flat(tab_number)

    return return_lst

if __name__ == '__main__':
    liste = [0, 10, 20, 3, 1, 3, 4, 5]
    #  Test de la fonction trie_stupide()
    print("------------------")
    print(trie_stupide(liste))
    # Test de la fonction trie_insertion()
    # print("------------------")
    # print(trie_insertion(liste, len(liste)))
    #  Test de la fonction insertion_sort()
    print("------------------")
    my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
    print('La liste avant tri', my_lst_to_sort)
    print('Le tri par sélection donne ', insertion_sort(my_lst_to_sort))
    #  Test de selection_sort()
    print("------------------")
    print('La liste avant tri', my_lst_to_sort)
    print('Le tri par sélection donne ', selection_sort(my_lst_to_sort))
    #  Test de buble_sort()
    print("------------------")
    my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
    print('Avant tri :', my_lst_to_sort)
    print('Resultat du tri :', buble_sort(my_lst_to_sort))
    print('Après le tri la liste d\'origine n\'a pas été modifiée: ', my_lst_to_sort)
    #  Test du trie par fusion
    print("------------------")
    my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
    print('Avant tri :', my_lst_to_sort)
    print('Resultat du tri :', trie_fusion(my_lst_to_sort))
    print('Après le tri la liste d\'origine n\'a pas été modifiée: ', my_lst_to_sort)
    #  Test du trie radix_sort()
    print("------------------")
    print('Avant tri :', my_lst_to_sort)
    print("Résultat : ", radix(my_lst_to_sort))
    print("liste de départ : ", my_lst_to_sort)
