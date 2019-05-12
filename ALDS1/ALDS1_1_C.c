#include <stdio.h>
#include <math.h>

int main(void){
    int num = 0;
    printf("2以上の自然数を入力\n");
    scanf("%d", &num);

    if (num == 2){
        printf("素数です¥n");
    }else if ((num < 2) || ( (num % 2) == 0)){
        printf("素数ではないです\n");
    }else{
        int i = 3;
        do{
            if ( (num % i) == 0 ){
                printf("素数ではないです\n");
            }
            i += 2;

        }while ( i <= sqrt(num));
        printf("素数です\n");

    }

    return 0;
}







