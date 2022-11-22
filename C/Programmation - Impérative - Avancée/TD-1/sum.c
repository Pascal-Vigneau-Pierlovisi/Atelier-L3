//
// Created by Pascal Vigneau on 22/11/2022.
//

#include <stdio.h>
#include <stdlib.h>

int main (int argc, char* argv[]){

    if(argc >=3){
        int sum = 0;
        for(int i = 1; i < argc; i++){
            if(atoi(argv[i]) != 0){
                sum += atoi(argv[i]);
            } else {
                printf("There is a problem with argument %d, %s.\n", i, argv[i]);
                return 0;
            }
        }
        printf("La somme est %d", sum);
    }
    else{
        printf("Wrong usage, expected 2 arguments.\n");
    }
    return 0;
}
