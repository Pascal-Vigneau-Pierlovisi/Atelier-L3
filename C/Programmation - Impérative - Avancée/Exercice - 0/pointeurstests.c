//
// Created by Pascal Vigneau on 07/11/2022.
//

#include <stdio.h>


int main(int argc, char const *argv[]){

    int type = 10;
    int *pt_sur_un_type = &type;

    printf("La valeur est %d \n", type);
    *pt_sur_un_type = 22;
    long int size = sizeof(pt_sur_un_type);
    printf("La valeur est %d \n", type);
    printf("Taille du pointeur : %lu \n", size);
}

