trouver = False

def Placer_Reine(Tab, n):
    global trouver
    if(n == 8):
        trouver = True
        return
    for i in range(8):
        if acceptable(Tab, n, i):
            Tab[n] = i
            Placer_Reine(Tab, n+1)
            if trouver:
                return
            Tab[n] = -1



def acceptable(Tab, n, i):





if __name__ == '__main__':
    Tab = [-1]*8

