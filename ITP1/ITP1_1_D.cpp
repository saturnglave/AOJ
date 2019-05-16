#include <iostream>
using namespace std;

int main(){
    int h = 0;
    int m = 0;
    int s = 0;

    cin >> s;
    h = s / 3600;
    m = (s % 3600) / 60;
    s = s % 60;

    cout << h << ":" << m << ":" << s << endl;

    return 0;
}