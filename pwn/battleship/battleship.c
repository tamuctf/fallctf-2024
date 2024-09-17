#include <stdio.h>
#include <inttypes.h>

int upkeep() {
        // IGNORE THIS
        setvbuf(stdin, NULL, _IONBF, 0);
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stderr, NULL, _IONBF, 0);
}

void win(){
	char flag[64];
	FILE* f = fopen("flag.txt", "r");
	if (!f) {
		perror("Could not read the flag!");
		return;
	}
	fgets(flag, sizeof(flag), f);
	puts(flag);
}

int main(){
	char buff[16];
	void (*guess)();

	upkeep();

	while(1){
		puts("Guess the address of the win function");
		if (scanf("%" SCNxPTR, &guess) != 1) {
        		puts("Invalid input");
        		return 1;
    		}

		if(guess < (void*)win){
			puts("Too low!");

		}else if(guess > (void*)win){
			puts("Too high!");
		
		}else{
			puts("Uh Oh!");
		}
		
		puts("Try again? (y/N)");
		
		int c;
		while ((c = getchar()) != '\n' && c != EOF);
		c = getchar();
		
		if(c != 'y'){
			break;
		}
	}

	puts("Now say goodbye:");
	
	gets();
	gets(&buff);

	return 0;
}

