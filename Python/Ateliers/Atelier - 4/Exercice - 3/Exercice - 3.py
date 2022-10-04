# Pascal, Python 3.10 | Développé le 15 Septembre 2022 sous l'IDE Pycharm
from random import randint


def choose_element_list(list_in_which_to_choose: list, old_choice) -> str | int | float:
    """
    La fonction choose_element_list() permet de prendre un élément au hasard dans list_in_which_to_choose

    :param list_in_which_to_choose(list): Représente la liste
    :return item(str|int|float): La valeur de retour peut être str, int ou float elle représente
    l'élément choisi au hasard.
    """

    choice = randint(0, len(list_in_which_to_choose) -1)

    item = list_in_which_to_choose[choice]

    while item == old_choice:

        choice = randint(0, len(list_in_which_to_choose) - 1)
        item = list_in_which_to_choose[choice]

    return item




if __name__ == '__main__':
    # Test de votre code
    old_choice = 0
    lst_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Liste triée de départ', lst_sorted)
    e1 = choose_element_list(lst_sorted, old_choice)
    print('A la première exécution', e1, 'a été sélectionné')
    old_choice = e1
    e2 = choose_element_list(lst_sorted, old_choice)
    print('A la deuxième exécution', e2, 'a été sélectionné')
    assert e1 != e2, "Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"
