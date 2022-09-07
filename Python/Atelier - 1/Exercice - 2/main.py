def estBissextile(data : int):

    if(data % 4 == 0 and data % 100 > 0):

        return f"L'année {data} est une année bissextile."

    if(data % 400 == 0):

        return f"L'année {data} est une année bissextile."

    else:

        return f"L'année {data} n'est pas une année bissextile."


if __name__ == '__main__':

    for i in range(0, 4000):
        print(estBissextile(i))



#print(estBissextile(int(input("Merci de mettre votre année : "))))