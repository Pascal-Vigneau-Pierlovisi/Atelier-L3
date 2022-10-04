# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm

def rangerVitrine(liste_objet: list, nb_emplacements: int) -> bool:
    """
    La fonction rangerVitrine() permet de ranger les vitrines du magasin avec les objets de la réserve

    :param liste_objet(list): Représente la liste des objets à ranger
    :param v_magasin(list): Représente la vitrine du magasin
    :param v_secours(list): Représente la vitrine de secours
    :return ranger(bool): La valeur de retour ranger est un  booléen indiquant que les listes ont bien été rangées
    """
    ranger = True  # Ranger est par défaut sur True sa valeur change si un doublon est rencontré
    limit = nb_emplacements  # Place max dans une vitrine
    liste_objet.sort()  # Triage de la liste

    if len(liste_objet) > nb_emplacements * 2:  # Vérification que la taille de la liste passé en paramètre
        ranger = False

    if doublon(liste_objet):  # Vérification de la présence de doublons dans la liste
        vitrine_1 = liste_objet[0:nb_emplacements]
        vitrine_2 = liste_objet[nb_emplacements:len(liste_objet)]
        for i in vitrine_1:
            vitrine_magasin.append(i)
        for s in vitrine_2:
            vitrine_secours.append(s)
        ranger = True

    else:

        while ranger and len(liste_objet) != 0:
            if liste_objet[0] not in vitrine_magasin and len(vitrine_magasin) != limit:
                vitrine_magasin.append(liste_objet[0])
                liste_objet.pop(0)

            if liste_objet[0] not in vitrine_secours and len(vitrine_secours) != limit:
                vitrine_secours.append(liste_objet[0])
                liste_objet.pop(0)

            if liste_objet[0] in vitrine_magasin and liste_objet[0] in vitrine_secours:
                print("DEBUG")
                ranger = False

    return ranger

def doublon(liste_objet: list) -> bool:
    """
    La fonction doublon() permet de savoir si des doublons sont présents dans liste_objet()

    :param liste_objet(list): Représente la liste à tester
    :return a_doublon(bool): La valeur de retour est un booléen permettant de savoir la présence de doublons ou non
    dans liste_objet
    """

    a_doublon = True  # La valeur par défaut est sur True

    for i in range(len(liste_objet) - 1):  # parcourt de la liste par rapport à son index
        if liste_objet[i] == liste_objet[i + 1]:
            a_doublon = False

    return a_doublon

def test_rangerVitrine(function : callable, case : int) -> bool:
    """
    La fonction test_rangerVitrine() permet de tester la fonction rangerVitrine()

    :param function(callable): Représente la fonction passée en paramètre
    :param case: Représente le n° du test qui va être fait
    :return res(bool): La valeur de retour est un booléen signifiant si le test est passé au non
    """
    res = True
    match case:
        case 1:  # Pour une liste vide passée en paramètre
            if(function == True):
                res = False
        case 2:  # Nombre de place < composition de la liste
            if(function == True):
                res = False
        case 3:  # Triplet présent dans la liste
            if(function == True):
                res = False
    return res

if __name__ == '__main__':
    print("------------RANGER VITRINE------------")

    liste_objets = [1, 3, 4, 5, 2, 0, 9, 10, 20, 30]
    vitrine_magasin = []
    vitrine_secours = []

    if (rangerVitrine(liste_objets, 5)):
        print("Tous les éléments ont pu être rangé !")
        print(vitrine_magasin)
        print(vitrine_secours)

    else:
        print("Pas tous les éléments ont pu être rangé :c, vous avez peut-être mis des triplons")


    assert test_rangerVitrine(rangerVitrine([], 5), 1) == False, "Une erreur est survenue pour une liste vide"

    assert test_rangerVitrine(rangerVitrine(liste_objets, 4), 2) == False, "Une erreur est survenue pas assez de place normalement"
