# Pascal, Python 3.10 | Développé le 19 Septembre 2022 sous l'IDE Pycharm
from random import randint
from time import perf_counter
from matplotlib import pyplot as plt


def sort_list(lst_param : list) -> list:
    """
    La fonction sort_list() permet de trier une liste dans l'ordre croissant

    :param lst_param(list): Représente la liste qui va être triée
    :return return_lst(list): La valeur de retour est une liste contenant les éléments trié
    """

    return_lst = []
    lst_height = len(lst_param)  # taille de la liste passée en paramètre

    while len(return_lst) != lst_height:
        basic_index = 0
        for i in range(len(lst_param)):
            if lst_param[i] < lst_param[basic_index]:
                basic_index = i
        return_lst.append(lst_param[basic_index])
        lst_param.pop(basic_index)

    return return_lst

def affiche_graph(moy_function_1 : list, moy_function_2 : list) -> None:
    """
    La procédure affiche_graph() permet d'afficher un graphique généré en fonction des différentes valeurs

    :param moy_function_1(list): Représente une liste contenant les moyennes sur les différents test
    :param moy_function_2(list): Représente une liste contenant les moyennes sur les différents test
    :param intervalle(list): Représente l'intervalle pour les tailles de liste
    """
    # Ici on décrit les abscisses
    # Entre 0 et 5 en 10 points
    x_axis_list = ["conf1", "conf2", "conf3"]
    fig, ax = plt.subplots()
    # Dessin des courbes, le premier paramètre
    # correspond aux point d'abscisse le
    # deuxième correspond aux points d'ordonnées
    # le troisième paramètre, optionnel permet de
    # choisir éventuellement la couleur et le marqueur
    ax.plot(x_axis_list, moy_function_1, 'bo-', label='fonction 1')
    ax.plot(x_axis_list, moy_function_2, 'r*-', label='fonction 2')

    ax.set(xlabel='Configuration', ylabel='Temps en ms',
           title="Différence de temps entre l'execution de la fonction 1 et fonction 2 ")
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    # fig.savefig("test.png")
    plt.show()

def time_for_fonction(function1 : callable, function2 : callable, conf : int) -> tuple:
    """
    La fonction time_for_function() permet de renvoyer la moyenne temps pour l'exécution de 2 fonctions

    :param function1(callable): Représente la première fonction
    :param function2(callable): Représente la deuxième fonction
    :param conf(int): la configuration de la liste qui va être testée
    :return time(tuple): La valeur de retour est un tuple contenant la moyenne de temps sur 10 execution des 2 fonctions
    """

    average_time_function_1 = 0
    average_time_function_2 = 0

    liste_test = []

    match conf:
        case 1:
            liste_test = [item for item in range(0, randint(0, 100))]  # Création d'une liste de grosse taille
        case 2:
            liste_test = [sorted(item for item in range(0, randint(0, 100)))] # Création d'une liste triée par défaut
        case 3:
            liste_test = [item for item in range(0, randint(0, 100))]  # Création d'une liste de grosse taille
            liste_test.sort(reverse=True)  # Trie inverse de la fonction


    for i in range(10):
        # ------------------
        start = perf_counter()
        function1(liste_test)
        end = perf_counter()
        average_time_function_1 = average_time_function_1 + (end-start)
        # ------------------
        start = perf_counter()
        function2(liste_test)
        end = perf_counter()
        average_time_function_2 = average_time_function_2 + (end-start)

    time = (average_time_function_1 / 10, average_time_function_2 / 10)

    return time

def with_sorted(lst_param : list) -> list:
    """
    La fonction with_sorted permet de trier une liste directement avec la fonction sorted que propre python

    :param lst_param(list): Représente la liste à trier
    :return return_lst(list): La valeur de retour est une liste triée
    """
    return_lst = sorted(lst_param)

    return return_lst

if __name__ == '__main__':
    #  Test du trie d'une liste
    print("------------")
    lst_trie = [10, 20, 1, 3, 4, 30, -1]  # Création de la liste
    print(sort_list(lst_trie))
    #  Test de comparaison des 2 fonctions de trie
    moyenne_fonction1 = []
    moyenne_fonction2 = []
    conf = [1, 2, 3]
    for i in conf:
        moyenne = time_for_fonction(sort_list, with_sorted, i)
        moyenne_fonction1.append(moyenne[0])
        moyenne_fonction2.append(moyenne[1])
    affiche_graph(moyenne_fonction1, moyenne_fonction2)


