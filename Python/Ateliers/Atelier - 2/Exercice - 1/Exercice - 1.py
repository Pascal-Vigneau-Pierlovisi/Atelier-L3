# Pascal, Python 3.10 | Développé le 8 Septembre 2022 sous l'IDE Pycharm

#utilisé dans la fonction moyenne()
def somme(liste:list)->float:
    """
    La fonction somme() permet de retourner la somme des valeurs d'une liste

    :param liste(list): Représente la liste contenant les différentes valeurs
    :return addition(float): Représente le résultat de la somme de tous les éléments d'une liste
    """

    addition = 0
    compteur = 0


    for i in liste:
        addition = addition + i

    """
    for i in range(len(liste)):
        addition += liste[i]
    """
    """
    while compteur < len(liste):

        addition = addition + liste[compteur]
        compteur+=1
    """

    return addition

def moyenne(liste:list)->float:
    """
    La fonction moyenne() permet de calculer la moyenne des éléments d'une liste

    :param liste(list): représente une liste de nombre
    :return average(float): La valeur de retour est un float représentant la moyenne des éléments de la liste
    """
    average = 0
    height = len(liste) - 1

    if(len(liste) != 0):
        average = somme(liste) / height


    return average

#utilisé dans la fonction moy_sup()
def nb_sup(L:list,e:float)->int:
    """
    La fontion nb_sup() permet de retourner le nombre d'éléments d'une liste L supérieurs à e

    :param L(list): Représente la liste d'entier / float à comparer
    :param e(float): Représente le float à comparer avec les éléments de la liste
    :return number(int): La valeur de retour est un entier représentant le nombre d'éléments de la liste L supérieur à e
    """

    number = 0
    height = len(L)

    if height != 0:

        """       
        for i in range(height):
            if L[i] > e:
                number+=1
        """

        for p in L:
            if p > e:
                number+=1

    return number

def moy_sup(L:list, e:float)->float:
    """
    La fonction moy_sup() permet de calculer la moyenne des éléments de la liste L supérieur à la valeur e

    :param L(list): Représente une liste d'élément
    :param e(float): Représente un float qui va être utilisé pour être comparé avec les éléments de la liste L
    :return average(float): La valeur de retour est un float qui représente la moyenne des éléments de la liste L > à e
    """
    average = 0
    elements_sup = nb_sup(L, e)
    height = len(L) - 1

    while height != elements_sup - 1:

        average = average + L[height]
        height-=1

    return average / elements_sup

def val_max(L:list)->float:
    """
    La fonction val_max() permet de retourner l'élément le plus grand de la liste L

    :param L(list): Représente une liste d'éléments
    :return maxi(float): La valeur de retour est un float représentant l'élément le plus grand de la liste L
    """
    maxi = L[0]
    longueur = len(L)
    indice_max = 0
    for i in range(longueur):
        if L[i] >= maxi:
            maxi = L[i]
            indice_max = i
    return maxi

def ind_max(L:list)->int:
    """
    La fonction ind_max() permet de retourner l'index de l'élément le plus grand de la liste L

    :param L(list): Représente une liste d'éléments
    :return indice_max(int): La valeur de retour est un int représentant l'index du plus grand élément de la liste L
    """
    indice_max = 0
    longueur = len(L)
    maxi = L[0]
    for i in range(longueur):
        if L[i] >= maxi:
            maxi = L[i]
            indice_max = i
    return indice_max

if __name__ == '__main__':
    print("TEST SOMME")
    # test liste vide
    print("Test liste vide : ", somme([]))  # test somme 11111
    S = [1, 10, 100, 4444443, 1000, 10000]
    print("Test somme 1111 : ", somme(S))
    # test moyenne liste vide
    print("Moyenne : ", moyenne([]))
    print("Moyenne : ", moyenne(S))
    # test nombre d'éléments supérieurs à 20 dans la liste S
    print(f"{nb_sup(S, 20)} éléments sont supérieurs à 20 dans cette liste ")
    # test moyenne des éléments supérieurs à 20 dans la liste S
    print(f"{moy_sup(S, 20)} est la moyenne des éléments > 20 dans cette liste ")
    # test valeur max de la liste S
    print(f"La valeur max de la liste est : {val_max(S)}")
    # test indice max de la liste S
    print(f"Voici l'indice de l'élément le plus grand de la liste S : {ind_max(S)}")


