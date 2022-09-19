# Pascal, Python 3.10 | Développé le 19 Septembre 2022 sous l'IDE Pycharm
import copy
from random import randint
from time import perf_counter

from matplotlib import pyplot as plt


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


def calc_time(height_list: int) -> tuple:
    """
    La fonction calc_time() permet de calculer les temps pour l'execution des différentes fonctions

    :param height_list(int): Représente la taille de la liste qui va être générée aléatoirement
    :return time(tuple): La valeur de retour est un tuple contenant les moyennes de temps des différents tests
    """

    average_time_trie_insertion = 0
    average_time_insertion_sort = 0
    average_time_selection_sort = 0
    average_time_buble_sort = 0
    average_time_trie_fusion = 0
    average_time_radix = 0



    lst = [item for item in range(0, height_list)]

    copy_lst = lst.copy()

    for i in range(10):
        # ------------------
        start = perf_counter()
        trie_insertion(copy_lst, len(copy_lst))
        end = perf_counter()
        average_time_trie_insertion = average_time_trie_insertion + (end - start)
        # ------------------
        copy_lst = lst.copy()
        start = perf_counter()
        insertion_sort(copy_lst)
        end = perf_counter()
        average_time_insertion_sort = average_time_insertion_sort + (end - start)
        # ------------------
        copy_lst = lst.copy()
        start = perf_counter()
        selection_sort(copy_lst)
        end = perf_counter()
        average_time_selection_sort = average_time_selection_sort + (end - start)
        # ------------------
        copy_lst = lst.copy()
        start = perf_counter()
        buble_sort(copy_lst)
        end = perf_counter()
        average_time_buble_sort = average_time_buble_sort + (end - start)
        # ------------------
        copy_lst = lst.copy()
        start = perf_counter()
        trie_fusion(copy_lst)
        end = perf_counter()
        average_time_trie_fusion = average_time_trie_fusion + (end - start)
        # ------------------
        copy_lst = lst.copy()
        start = perf_counter()
        radix(copy_lst)
        end = perf_counter()
        average_time_radix = average_time_radix + (end - start)


    time = (average_time_trie_insertion / 10, average_time_insertion_sort / 10, average_time_selection_sort / 10,
            average_time_buble_sort / 10, average_time_trie_fusion / 10, average_time_radix / 10)

    return time

def affiche_graph(moyenne_trie_insertion: list, moyenne_insertion_sort: list, moyenne_selection_sort:list, moyenne_buble_sort: list, moyenne_trie_fusion:list, moyenne_radix: list, intervalle: list) -> None:
    """
    La procédure affiche_graph() permet d'afficher un graphique généré en fonction des différentes valeurs

    :param moyenne_trie_insertion: Représente la moyenne des résultats de cette fonction
    :param moyenne_insertion_sort: Représente la moyenne des résultats de cette fonction
    :param moyenne_selection_sort: Représente la moyenne des résultats de cette fonction
    :param moyenne_buble_sort: Représente la moyenne des résultats de cette fonction
    :param moyenne_trie_fusion: Représente la moyenne des résultats de cette fonction
    :param moyenne_radix: Représente la moyenne des résultats de cette fonction
    :param intervalle(list): Représente l'intervalle pour les tailles de liste
    """
    # Ici on décrit les abscisses
    # Entre 0 et 5 en 10 points
    x_axis_list = intervalle
    fig, ax = plt.subplots()
    # Dessin des courbes, le premier paramètre
    # correspond aux point d'abscisse le
    # deuxième correspond aux points d'ordonnées
    # le troisième paramètre, optionnel permet de
    # choisir éventuellement la couleur et le marqueur
    ax.plot(x_axis_list, moyenne_trie_insertion, 'bo-', label='trie_insertion')
    ax.plot(x_axis_list, moyenne_insertion_sort, 'r*-', label='_insertion_sort')
    ax.plot(x_axis_list, moyenne_selection_sort, 'g', label='selection_sort')
    ax.plot(x_axis_list, moyenne_buble_sort, 'y', label='buble_sort')
    ax.plot(x_axis_list, moyenne_trie_fusion, 'k', label='trie_fusion')
    ax.plot(x_axis_list, moyenne_radix, 'c', label='radix')

    ax.set(xlabel='Taille des listes', ylabel='Temps en ms',
           title="Différence de temps entre l'execution des différentes fonctions ")
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    # fig.savefig("test.png")
    plt.show()


if __name__ == '__main__':
    intervalle = [5, 10, 100, 1000]  # Taille des listes
    moyenne_trie_insertion = []
    moyenne_insertion_sort = []
    moyenne_selection_sort = []
    moyenne_buble_sort = []
    moyenne_trie_fusion = []
    moyenne_radix = []

    for i in intervalle:
        moyenne = calc_time(i)
        moyenne_trie_insertion.append(moyenne[0])
        moyenne_insertion_sort.append(moyenne[1])
        moyenne_selection_sort.append(moyenne[2])
        moyenne_buble_sort.append(moyenne[3])
        moyenne_trie_fusion.append(moyenne[4])
        moyenne_radix.append(moyenne[5])
    affiche_graph(moyenne_trie_insertion, moyenne_insertion_sort, moyenne_selection_sort, moyenne_buble_sort,
                  moyenne_trie_fusion, moyenne_radix, intervalle)


