using namespace std;

#include <iostream>
#include <vector>
#include "numbth.hpp"



int main() {

    vector<unsigned long long> v0 = {1,2,3,4,6};
    vector<unsigned long long> v1 = {4,6};

    unsigned long long a = 102;
    unsigned long long b = 54;


    cout << "GCD(" << a << ", " << b << ") = " << gcd(a,b) << endl;


    cout << "LCM(";
    for(unsigned long long x : v0) {
        cout << x << ", ";
    }
    cout << ") = " << lcm(v0) << endl;


    cout << "LCM(";
    for(unsigned long long x : v1) {
        cout << x << ", ";
    }
    cout << ") = " << lcm(v1) << endl;


    cout << "LCM_2(" << a << ", " << b << ") = " << lcm_2(a, b) << endl;


    return 0;
}
