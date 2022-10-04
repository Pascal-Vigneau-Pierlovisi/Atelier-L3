tab_imc = [16.5, 18.5, 25.0, 30.0, 35.0, 40.0]
tab_mess = ["dénutrition ou famine", "maigreur", "corpulence normale", "surpoids", "obésité modérée", "obésité sévère", "obésité morbide"]


def messageImc(imc:float):
    compteur  = 0
    for a in range(0,len(tab_imc)):

        #print(tab_imc[a])

        if(imc > tab_imc[a]):
            compteur+=1

    print(compteur)

    return tab_mess[compteur]

if __name__ == '__main__':

    imc = float(input("Merci de mettre votre imc : "))
    print(messageImc(imc))




