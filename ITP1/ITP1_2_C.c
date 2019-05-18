#include <stdio.h>

void swap(int *num1, int *num2){
    int tmp = *num1;
    if(*num1 > *num2){
        *num1 = *num2;
        *num2 = tmp;
    }
}

int main(){
    int a, b, c = 0;
    scanf("%d %d %d", &a, &b, &c);

    if(a > b){
        swap(&a, &b);
    }
    if(b > c){
        swap(&b, &c);
    }
    if(a > b){
        swap(&a, &b);
    }

    printf("%d %d %d\n", a, b, c);
    return 0;
}