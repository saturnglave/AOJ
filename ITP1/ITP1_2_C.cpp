#include <iostream>
using namespace std;
void swap(int &num1, int &num2){
    int tmp = num1;
    if(num1 > num2){
        num1 = num2;
        num2 = tmp;
    }
}

int main(){
    int a, b, c = 0;
    cin >> a >> b >> c;

    if(a > b){
        swap(a, b);
        //cout << a << " " << b << " " << c << endl;  
    }
    if(b > c){
        swap(b, c);
        //cout << a << " " << b << " " << c << endl;
    }
    if(a > b){
        swap(a, b);
        //cout << a << " " << b << " " << c << endl;
    }

    cout << a << " " << b << " " << c << endl;

    
    return 0;
}