#  Pascal Vigneau Pierlovisi, le 4 Octobre 2022
TA = [5, 4, 3, 2, 1]
TB = []
TC = []
N = len(TA)

def Hanoi(N, TA, TB, TC, NomA, NomB, NomC):
    if N==1:
        TB.append(TA[-1])
        del TA[-1]
        print(f'Déplace {TB[-1]} de {NomA} vers {NomB}')
    else:
        Hanoi(N-1, TA, TC, TB, NomA, NomC, NomB)
        Hanoi(1, TA, TB, TC, NomA, NomB, NomC)
        Hanoi(N-1, TC, TB, TA, NomC, NomB, NomA)

if __name__ == '__main__':
    Hanoi(N, TA, TB, TC, "TA", "TB", "TC")
    print(TB)

