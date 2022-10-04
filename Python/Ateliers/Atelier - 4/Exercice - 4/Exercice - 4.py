# Pascal, Python 3.10 | Développé le 15 Septembre 2022 sous l'IDE Pycharm
from random import randint


def extract_elements_list(list_in_which_to_choose : list, int_nbr_of_element_to_extract : int) -> list:
    """
    La fonction extract_elements_list() permet de prendre un nombre int_nb_of_elements_to_extract d'éléments
    aléatoirement dans list_in_which_to_choose

    :param list_in_which_to_choose(list): Représente la liste
    :param int_nbr_of_element_to_extract(int): Représente le nombre d'éléments qui vont être pris aléatoirement
    :return back_list(list): La valeur de retour est une liste contenant des éléments tirée aléatoirement
    """

    back_list = []

    for i in range(int_nbr_of_element_to_extract):
        rand = randint(0, len(list_in_which_to_choose) - 1)
        back_list.append(list_in_which_to_choose[rand])

    return back_list

if __name__ == '__main__':
    # Test de votre code
    lst_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print('Liste de départ', lst_sorted)
    sublist = extract_elements_list(lst_sorted, 5)
    print('La sous liste extraite est', sublist)
    print('Liste de départ après appel de la fonction est', lst_sorted)