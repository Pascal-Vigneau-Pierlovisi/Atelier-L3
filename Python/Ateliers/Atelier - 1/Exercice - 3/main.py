from math import sqrt

def discriminant(a:int, b:int, c:int):

    return ((b**b) - (4*a*c))

def racine_unique(a, b):

    return(-b/(2*a))

def racine_double(a,b,delta,num:int):

    if(num == 1):


        return ((-b + sqrt(delta))//(2*a))

    else:

        return ((-b - sqrt(delta))//(2*a))

def str_equation(a:int, b:int, c:int):
    return(f"{a}x2 + ({b}x) + {c}=0")

def solution_equation(a, b, c):

    delta = discriminant(a, b, c)

    if(delta < 0):
       return("Pas de solutions pour l'équation : ", str_equation(a,b,c))

    if(delta == 0):
        return("Une solution x1 = ", racine_unique(a, b), " Pour l'équation : ", str_equation(a,b,c))

    else:
        return("Deux solutions x1 = ", racine_double(a, b, c, 1), " x2 = ", racine_double(a, b, c, 1), " Pour l'équation : ", str_equation(a,b,c))

def equation(a, b, c):
    print(solution_equation(a, b, c))

if __name__ == '__main__':
    equation(1, 1, 1)

