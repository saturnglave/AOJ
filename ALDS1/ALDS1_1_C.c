#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//素数判定。合成数xはp<=sqrt(x)を満たす素因子pをもつので、
//2からsqrt(x)まで割り切れるか調べれば良い
int main(void){
    int num = 0;
    printf("2以上の自然数を入力\n");
    scanf("%d", &num);

    if (num == 2){
        //2は素数
        printf("素数です¥n");
    }else if ((num < 2) || ( (num % 2) == 0)){
        //1, 0と負の数は素数ではない。また2以外の偶数も素数ではない
        printf("素数ではないです\n");
    }else{
        //3から調べる。ただし偶数では割り切れてしまうので割る数を2ずつ増やす
        //sqrt(num)まで続けて割り切れなければ素数
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
