#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int reverse(int num);
int len(int num, int count);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, one, two, out = 0;
    std::cin >> n;
    for(int i = 0; i < n; i++){
        std::cin >> one >> two;
        reverse(one);
        reverse(two);
        out = reverse(one+two);
        std::cout << out;
    }
    return 0;
}

int reverse(int num){
    int temp = 0, N;
    N = len(num) - 1
    while (num > 0){
        temp += (num%10)*pow(10,N);
        N/=10;
        num/=10;
    }
}

int len(int num, int count){
    if (num <= 0) return count;
    return len(num/10, count+1);
}