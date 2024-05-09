#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned char shuffled[] = {
    '_', 'b', 'm', '_', '4', 'A', 'd', 'g', 'e', 'a', 'g', '1', '4', 'g', 'm', 'g', 'c', 'n', '3', 'r', 'a', '}', 'i', 'n', 'l', '_', '4', 'n', '{', '1', 'd', 's'
    };
    unsigned char perm1[] = {8, 20, 26, 28, 31, 11, 7, 0, 25, 30, 22, 3, 16, 5, 4, 1, 18, 19, 13, 6, 10, 2, 24, 27, 17, 23, 9, 15, 14, 29, 21, 12};
    unsigned char perm2[] = {17, 27, 31, 29, 10, 0, 8, 14, 15, 26, 18, 22, 6, 13, 5, 23, 9, 12, 7, 30, 11, 24, 2, 21, 1, 3, 4, 20, 25, 19, 28, 16};

    unsigned char flag[33];

    printf("What's the flag? ");
    fflush(stdout);
    fgets(flag, 33, stdin);


    for (int i = 0; i < 32; i++) {
        flag[32] |= shuffled[i] != flag[perm2[perm1[i]]];
    }
    
    if (flag[32]) {
        printf("Nope!\n");
    } else {
        printf("Correct!\n");
    }

    return 0;
}