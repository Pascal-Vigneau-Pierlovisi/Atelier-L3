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

    for i in liste_objet:
        if len(vitrine_magasin) - 1 != limit or len(vitrine_secours) - 1 != limit:

            if i not in vitrine_magasin or i not in vitrine_secours:
                if i not in vitrine_magasin and len(vitrine_magasin) - 1 < limit:
                    vitrine_magasin.append(i)
                else:
                    if i not in vitrine_secours and len(vitrine_secours) -1 < limit:
                        vitrine_secours.append(i)
            else:
                ranger = False
        else:
            ranger = False



    return ranger



if __name__ == '__main__':
    print("------------RANGER VITRINE------------")

    liste_objets = [1, 1, 2, 3, 4, 6, 7, 8, 9, 10]
    vitrine_magasin = []
    vitrine_secours = []

    print()

    if(rangerVitrine(liste_objets, 4)):
        print("Tous les éléments ont pu être rangé !")

    else:
        print("Pas tous les éléments ont pu être rangé :c")

    print(vitrine_magasin)
    print(vitrine_secours)

