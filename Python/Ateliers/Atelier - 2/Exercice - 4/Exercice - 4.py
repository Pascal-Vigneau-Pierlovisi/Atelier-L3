# Pascal, Python 3.10 | Développé le 11 Septembre 2022 sous l'IDE Pycharm

import matplotlib.pyplot as plt

def histo(F:list)->list:
    """
    La fonction histo() permet de créer une liste H qui va contenir le nombre de fois où un tiroir est pris

    :param F(list): Représente les une liste contenant les indexs des tiroirs
    :return H(list): La valeur de retour est une liste contenant le nombre d'apparition de chaque tiroir rangé dans l'ordre
    """

    maximum = max(F) + 1
    H = [0] * maximum

    for i in F:

        H[i] += 1

    return H

def est_injective(F:list)->bool:
    """
    La fonction est_injective() permet de déterminer si F est une injection

    :param F(list): Représente la fonction F
    :return injective(bool): La valeur de retour est un booléen True | False qui représente si F est injective ou non
    """
    injective = True

    max = len(F)
    i = 0

    while injective and i < max:
        if F[i] > 1:
            injective = False
        i+=1

    return injective

def est_surjective(F:list)->bool:
    """
    La fonction est_surjective() permet de déterminer si la fonction F est surjective

    :param F(list): représente la fonction F
    :return surjective(bool): La valeur de retour est un booléen qui représente le fait de savoir si F est surjective
    """

    surjective = True

    max = len(F)
    i = 0

    while surjective and i < max:
        if F[i] < 1:
            surjective = False
        i += 1

    return surjective

def est_bijective(F:list)->bool:
    """
    La fonction est_bijective() permet de déterminer si la fonction F est bijective

    :param F(list): Représente la fonction F
    :return bijective(bool): La valeur de retour est un booléen True | False qui permet de savoir si F est bijective
    """

    bijective = True

    injective = est_injective(histo(F))
    surjective = est_surjective(histo(F))

    if  not injective or not surjective:
        bijective = False

    return bijective

def afficheHisto(F:list)->None:
    """
    La procédure afficheHisto() permet de faire un affichage graphique de la fonction F

    :param F(list): Représente la fonction F
    :return: Rien n'est retourné c'est juste de l'affichage
    """
    print("TEST HISTOGRAMME")
    print(f"\nF={F}")

    H = histo(F)
    MAXOCC = max(H)
    for i in range(MAXOCC, -1, -1):
        for j in range(0, len(H), 1):
            if H[j] > i:
                print(" # |", end='')
            else:
                print("   |", end='')
        print("\n")

    for b in range(max(f) + 1):
        print(f" {b} |", end='')

def afficheHistoBis(F:list)->None:
    plt.hist(F)
    plt.title('Histogramme avec MatPlotLib')
    plt.show()

if __name__ == '__main__':
    # Initialisation de la liste liée aux tiroirs
    f = [0,6,5,6,9,4,2,1,5] # n'est pas injective
    j = [6, 1, 2, 5] # est injective
    h = [0, 1, 2, 3, 4, 5, 6, 7] # est injective et surjective donc bijective
    # Test de l'histogram
    print(histo(f))
    # Test pour savoir si f et j sont injectives
    print("-----------INJECTIVE-------------")
    print(est_injective(histo(f)))
    print(est_injective(histo(j)))
    # Test pour savoir si f et h sont surjectives
    print("-----------SURJECTIVE-------------")
    print(est_surjective(histo(j)))
    print(est_surjective(histo(h)))
    # Test pour savoir si f et h sont bijectives
    print("------------BIJECTIVE------------")
    print(est_bijective(f))
    print(est_bijective(h))
    # Test affichage de l'histogramme version 1
    print("------------HISTOGRAMME 1------------")
    print(afficheHisto(f))
    # Test affichage de l'histogramme version 2
    print("------------HISTOGRAMME 2------------")
    print(afficheHistoBis(f))