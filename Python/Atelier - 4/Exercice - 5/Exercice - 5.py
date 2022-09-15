# Pascal, Python 3.10 | Développé le 15 Septembre 2022 sous l'IDE Pycharm
from time import perf_counter

import matplotlib.pyplot as plt
import copy
import random


def mix_list(list_to_mix: list) -> list:
    """
    La fonction mix_list() permet de mélanger une liste

    :param list_to_mix(list): Représente la liste à mélanger
    :return new_list(list): La valeur de retour est une copie de la précédente liste mélangée
    """

    new_list = copy.deepcopy(list_to_mix)  # On crée une copie approfondie de liste_to_mix.

    for i in range(len(new_list) - 1, 0, -1):  # On parcourt la liste de la fin à son début

        rand = random.randint(0, i)  # On génère un entier aléatoire entre 0 et i + 1 pour avoir un intervalle qui
        # va changer à chaque incrémentation de i.

        new_list[rand], new_list[i] = new_list[i], new_list[rand] # On mélange la liste en switchant les index des
        # 2 cotés

    return new_list

def mix_list_shuffle(list_to_mix: list) -> list:
    """
    La fonction mix_list_shuffle() permet de mélanger une liste via le module random de python

    :param list_to_mix(list): Représente la liste à mélanger
    :return new_list(list): La valeur de retour est une copie de la précédente liste mélangée
    """

    new_list = copy.deepcopy(list_to_mix)
    random.shuffle(new_list)

    return new_list

def time_for_fonction(function1 : callable, function2 : callable, taille_liste : int) -> tuple:
    """
    La fonction time_for_function() permet de renvoyer la moyenne temps pour l'exécution de 2 fonctions

    :param function1(callable): Représente la première fonction
    :param function2(callable): Représente la deuxième fonction
    :param taille_liste(int): Représente la taille des listes qui vont être testées
    :return time(tuple): La valeur de retour est un tuple contenant la moyenne de temps sur 50 execution des 2 fonctions
    """

    average_time_function_1 = 0
    average_time_function_2 = 0

    liste_test = [item for item in range(0, taille_liste)]

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

def affiche_graph(moy_function_1 : list, moy_function_2 : list, intervalle : list) -> None:
    """
    La procédure affiche_graph() permet d'afficher un graphique généré en fonction des différentes valeurs

    :param moy_function_1(list): Représente une liste contenant les moyennes sur les différents test
    :param moy_function_2(list): Représente une liste contenant les moyennes sur les différents test
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
    ax.plot(x_axis_list, moy_function_1, 'bo-', label='fonction 1')
    ax.plot(x_axis_list, moy_function_2, 'r*-', label='fonction 2')

    ax.set(xlabel='Taille des listes', ylabel='Temps en ms',
           title="Différence de temps entre l'execution de la fonction 1 et fonction 2 ")
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    # fig.savefig("test.png")
    plt.show()

if __name__ == '__main__':
    # Calcule sur des listes de différentes tailles
    intervalle = [5, 10, 100, 1000, 10000, 100000] # Taille des listes
    moyenne_fonction1 = []
    moyenne_fonction2 = []

    for i in intervalle:
        moyenne = time_for_fonction(mix_list, mix_list_shuffle, i)
        moyenne_fonction1.append(moyenne[0])
        moyenne_fonction2.append(moyenne[1])
    affiche_graph(moyenne_fonction1, moyenne_fonction2, intervalle)




