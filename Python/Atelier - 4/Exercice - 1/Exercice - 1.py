# Pascal, Python 3.10 | Développé le 14 Septembre 2022 sous l'IDE Pycharm
from random import randint


def gen_list_random_int(int_nbr: int = 10, int_binf: int = 0, int_bsup: int = 10):
    """
    La fonction gen_list_random_int() permet de générer int_nbr entiers compris entre int_binf et int_bsup
    par défaut, les valeurs sont de 10 entiers compris entre 0 et 10

    :param int_nbr(int): Représente le nombre de nombres qui vont être générés. Par défaut 10
    :param int_binf(int): Représente un entier qui va être pris pour générer aléatoirement une liste d'entier
    (nombre inférieur)
    :param int_bsup(int): Représente un entier qui va être pris pour générer aléatoirement une liste d'entier
    (nombre supérieur)
    :return gen_list_random_int(list): la valeur de retour est une liste d'entiers qui ont étés générés aléatoirement
    en fonction des paramètres de la fonction.
    """
    gen_list_random_int = []

    for i in range(int_nbr):
        gen_list_random_int.append(randint(int_binf, int_bsup - 1))

    return gen_list_random_int


if __name__ == '__main__':
    # Test de la fonction gen_list_random_int()
    print("---------------")
    print(gen_list_random_int())  # Test de la fonction sans aucun paramètre

