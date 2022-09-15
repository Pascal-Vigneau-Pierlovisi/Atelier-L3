# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm
from math import *

def rangerVitrine(liste_objet: list, nb_emplacements: int) -> bool:
    """
    La fonction rangerVitrine() permet de ranger les vitrines du magasin avec les objets de la réserve

    :param liste_objet(list): Représente la liste des objets à ranger
    :return ranger(bool): La valeur de retour ranger est un  booléen indiquant que les listes ont bien été rangées
    """
    ranger = True  # Ranger est par défaut sur True sa valeur change si un doublon est rencontré
    limit = nb_emplacements  # Place max dans une vitrine
    liste_objet.sort()  # Triage de la liste

    while ranger and len(liste_objet) != 0:
        if liste_objet[0] not in vitrine_magasin and len(vitrine_magasin) != limit:
            vitrine_magasin.append(liste_objet[0])
            liste_objet.pop(0)

        if liste_objet[0] not in vitrine_secours and len(vitrine_secours) != limit:
            vitrine_secours.append(liste_objet[0])
            liste_objet.pop(0)

        else:
            ranger = False

    return ranger


if __name__ == '__main__':
    print("------------RANGER VITRINE------------")

    liste_objets = [1, 3, 4, 5, 2, 1, 0, 0, 10, 10, 9, 9]
    vitrine_magasin = []
    vitrine_secours = []

    if (rangerVitrine(liste_objets, 6)):
        print("Tous les éléments ont pu être rangé !")

    else:
        print("Pas tous les éléments ont pu être rangé :c")

    print(vitrine_magasin)
    print(vitrine_secours)

    print(rangerVitrine(liste_objets, 6))
