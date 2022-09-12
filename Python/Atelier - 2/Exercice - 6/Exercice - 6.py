# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm

# ---------------Partie 1--------------------
def present(L:list, e:float)->bool:
    """
    La fonction present() permet de déterminer si le float e est présent dans la liste L

    :param L(list): Représente une liste de float
    :param e(float): Représente le float cherché dans la liste L
    :return:
    """

    trouve = False

    for i in L:
        if i == e:
            trouve = True

    return trouve

#VERSION 1
def present1(L, e)->bool:

    value = False

    for i in range(0, len(L), 1):
        if(L[i] ==e):
            value = True

    return value

#VERSION 2
def present2(L, e)->bool:
    b = False
    for i in range(0, len(L), 1):
        if L[i] == e:
            b = True
    return b

#VERSION 3
def present3(L, e)->bool:

    b = False
    for i in range(0, len(L), 1):
        if L[i] == e:
            b = True

    return b

#VERSION 4
def present4(L, e)->bool:
    b = False
    i = 0
    while i < len(L) and b == False:
        if(L[i] == e):
            b = True
        i+=1
    return b

def test_present(present:callable, message:str, test: int)->None:
    """
    test_present() permet de faire des tests sur une fonction passée en paramètre

    :param present(callable): Représente la fonction passée en paramètre
    :param message(str): Représente le message à passer pour les erreurs ou success
    :param test(int): Représente le type de test à faire
    :return: Aucune valeur de retour
    """

    if test == 1:

        if(present):
            print(f"SUCCESS : {message}")


        else:
            print(f"ECHEC : {message}")

    if test == 2:

        if(present):
            print(f"ECHEC : {message}")

        else:
            print(f"SUCCESS : {message}")

# ---------------Partie 2--------------------

def pos(L:list, e:float)->list:
    """
    La fonction pos() permet de renvoyer l'index où se trouve l'élément e

    :param L(list): Représente la liste
    :param e(float): Représente le nombre à chercher
    :return position(list): La valeur de retour est une liste qui contient la position de e dans L.
    """

    position = []

    for i in range(len(L)):
        if L[i] == e:
            position.append(i)

    return position

#VERSION 1
def pos1(L, e) :

    Lres = []
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres += [i]
    return Lres

# VERSION 2
def pos2(L, e) :
    Lres = []
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres

# VERSION 3
def pos3(L, e) :
    Lres = []
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres

# VERSION 4
def pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[j]= i
    return Lres

def test_pos(pos:callable, message:str, test:int)->None:
    """
    La fonction test_pos() permet de faire des tests sur une fonction

    :param pos(callable): Représente la fonction à tester
    :param message(str): Représente le message à passer pour les erreurs ou success
    :param test(int): Représente le type de test à faire
    :return: Pas de valeur de retour, c'est une prodédure
    """

    if test == 1:

        if(pos):
            print(f"SUCCESS : {message}")

        else:
            print(f"ECHEC : {message}")

    if test == 2:

        if (pos):
            print(f"ECHEC : {message}")

        else:
            print(f"SUCCESS : {message}")

if __name__ == '__main__':
    LISTE = [0, 1, 2, 3, 4]
    # Test de la fonction present pour vérifier la présence de 4 et 5 dans LISTE
    print("4 est présent dans LISTE : ", present(LISTE, 4))
    print("5 est présent dans LISTE : ", present(LISTE, 5))
    # Test de la fonction de test
    print("-----------------------------")
    test_present(present4([], 2), "test liste vide", 2)
    test_present(present4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), "test debut", 1)
    test_present(present4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), "test milieu", 1)
    test_present(present4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), "test fin", 1)
    test_present(present4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), "test absence", 2)
    # Partie 2
    print("-----------------------------")
    test_pos(pos4([], 1), "test liste vide", 2)
    test_pos(pos4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), "test debut", 1)
    test_pos(pos4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), "test milieu", 1)
    test_pos(pos4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), "test fin", 1)
    test_pos(pos4([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), "test absence", 2)





