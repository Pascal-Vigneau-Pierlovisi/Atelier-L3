#include <stdio.h>
#include <stdlib.h>


void usage(){
	printf("usage: ba <filename>\n");
	exit(1);
}

int main(int argc, char **argv){
	if(argc != 2){
		usage();
	}
}
