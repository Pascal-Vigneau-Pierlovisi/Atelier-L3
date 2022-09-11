# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm

def separer(L:list)->list:
    """
    La fonction separer() permet de créer une nouvelle liste où les négatifs seront à gauche les nuls au milieu et les positifs à droite

    :param L(list):
    :return liste(list):
    """
    liste = []
    separateur = 0

    for i in L:
        if i <  0:
            liste.insert(0, i)
            separateur +=1
        elif i == 0:
            liste.insert(separateur, i)

        else:

            liste.append(i)

    return liste




if __name__ == '__main__':
    # Initialisation de la liste L
    L = [-1, 2, 10, 0, -2, 0, 4, - 199, 0, 10]
    # Test du trie de la liste L
    print(separer(L))

