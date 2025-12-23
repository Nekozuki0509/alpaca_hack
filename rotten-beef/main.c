// gcc -o chal main.c -O0

#include <stdio.h>
#include <unistd.h>

int main(void) {
    int key = 0xdead, dummy = 0xdead;
    char buffer[12];
    printf("input > ");
    scanf("%11s", buffer);
    printf("Your input: ");
    printf(buffer, &key, &dummy); // !?
    printf("\n");
    if(key == 0xbeef){
        printf("key = 0x%x (dummy = 0x%x), ok!\n", key, dummy);
        printf("Congratulations! spawning shell...\n");
        execve("/bin/sh", NULL, NULL);
    }
    else{
        printf("key = 0x%x (dummy = 0x%x), try again!\n", key, dummy);
    }
    return 0;
}

__attribute__((constructor))
void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
}