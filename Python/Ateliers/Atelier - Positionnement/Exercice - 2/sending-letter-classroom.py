#Pascal, 3.10 | Developpé sous l'IDE Pycharm le 8 Septembre 2022 | Le code n'est pas finit
"""
Une fonction pour le calcul -> computePrice()
Une fonction qui permet de récupérer les différents prix -> getPrice()
Une fonction principale qui va appeler la fonction calcul du prix -> main()
"""
TARIF_LETTRE_VERTE = {
    "20": 1.16,
    "100": 2.32,
    "250": 4,
    "500": 6,
    "1000": 7.50,
    "3000": 10.50
}
TARIF_COMPLEMENT_LETTRE_VERTE = {
    "OM1": 0.05,
    "OM2": 0.11
}
TARIF_LETTRE_ECO_PLI = {
    "20": 1.14,
    "100": 2.28,
    "250": 3.92
}
TARIF_COMPLEMENT_ECO_PLI = {
    "OM1": 0.02,
    "OM2": 0.05
}

def getPrice(letter_type:int, weight:float)->float:
    """
    La fonction permet de renvoyer le prix net d'une lettre en fonction de son type et de son poids

    :param letter_type(int):type de lettre 1: Lettre verte 2 Lettre eco-pli
    :param weight(float):poids de la lettre
    :return: prix_net(float)
    """
    prix_net = 0
    liste_cles = []
    liste = {}
    if letter_type == 1:
        liste_cles = list(TARIF_LETTRE_VERTE.keys())
        liste = TARIF_LETTRE_VERTE
    elif letter_type == 2:
        liste_cles = list(TARIF_LETTRE_ECO_PLI.keys())
        liste = TARIF_LETTRE_ECO_PLI

    for i in range(len(liste_cles) - 1):
        if float(liste_cles[i]) < weight <= float(liste_cles[i + 1]):
            prix_net = liste[liste_cles[i + 1]]





    return prix_net





if __name__ == '__main__':

    print(getPrice(1, 112))

