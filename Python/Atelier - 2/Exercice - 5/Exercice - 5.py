# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm

def rangerVitrine(liste_objet:list)->bool:
    """
    La fonction rangerVitrine() permet de ranger les vitrines du magasin avec les objets de la réserve

    :param liste_objet(list): Représente la liste des objets à ranger
    :return: La valeur de retour est True pour signifier que les objets ont étés rangés
    """

    for i in liste_objet:
        if i not in vitrine_magasin:
            vitrine_magasin.append(i)
        else:
            vitrine_secours.append(i)

    return True



if __name__ == '__main__':
    print("------------RANGER VITRINE------------")

    liste_objets = [1, 1, 2, 4, 5, 7, 9]
    vitrine_magasin = []
    vitrine_secours = []

    rangerVitrine(liste_objets)
    
    print(vitrine_magasin)
    print(vitrine_secours)

