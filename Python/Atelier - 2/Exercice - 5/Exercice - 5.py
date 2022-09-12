# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm

from math import *

def rangerVitrine(liste_objet:list, nb_emplacements:int)->bool:
    """
    La fonction rangerVitrine() permet de ranger les vitrines du magasin avec les objets de la réserve

    :param liste_objet(list): Représente la liste des objets à ranger
    :return ranger(bool): La valeur de retour ranger est un  booléen indiquant que les listes ont bien été rangées
    """
    ranger = True
    limit = nb_emplacements
    nb_item_objet_reparti = ceil((len(liste_objet))/2)


    if(nb_item_objet_reparti > limit):

        ranger = False

    else:
        for i in liste_objet:
            if len(vitrine_magasin) - 1 == limit and len(vitrine_secours) - 1 == limit:
                ranger = False
            else:
                if i not in vitrine_magasin:
                    vitrine_magasin.append(i)
                else:
                    if i not in vitrine_secours:
                        vitrine_secours.append(i)

    print(len(vitrine_magasin))

    return ranger



if __name__ == '__main__':
    print("------------RANGER VITRINE------------")

    liste_objets = [1, 1, 1, 1, 5, 7, 9, 9, 9, 10, 11]
    vitrine_magasin = []
    vitrine_secours = []

    print(rangerVitrine(liste_objets, 5))

    print(vitrine_magasin)
    print(vitrine_secours)

