using namespace std;

#include <vector>
#include <iostream>  // TODO remove

//typedef long long = int;

// TODO should be using boost/math/common_factor.hpp
unsigned long long gcd(unsigned long long a, unsigned long long b);

unsigned long long lcm_2(unsigned long long a, unsigned long long b);

unsigned long long lcm(vector<unsigned long long> v);


unsigned long long gcd(unsigned long long a, unsigned long long b) {
    unsigned long long x = a;
    unsigned long long y = b;
    unsigned long long tmp;

    while(y != 0) { // while(y):?
        tmp = y; // TODO fancy swap in C++11?
        y = x % y;
        x = tmp;
    }
    return a;
}


unsigned long long lcm_2(unsigned long long a, unsigned long long
                         b) {
    return a * b / gcd(a, b);
}


unsigned long long lcm(vector<unsigned long long> v) {
    for(int i=0; i<v.size(); i++) {
        unsigned long long tmp0;
        unsigned long long tmp1;

        tmp0 = v[v.size()-1];
        v.pop_back();
        tmp1 = v[v.size()-1];
        v.pop_back();

        v.push_back(lcm_2(tmp0, tmp1));
    }
    for(unsigned long long x : v)
        cout << x;
}
