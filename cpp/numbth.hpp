using namespace std;

long long gcd(long long a, long long b);

long long lcm_2(long long a, long long b);

long long lcm(vector<long long> v);


long long gcd(long long a, long long b) {
    long long tmp;
    while(b != 0) { // while(b):?
        tmp = b; // TODO fancy swap in C++11?
        b = a % b;
        a = tmp;
    }
    return a
}


long long lcm_2(long long a, long long b) {
    return a * b / gcd(a, b)
}


long long lcm(vector<long long> v) {
    if(len(v) == 2) {
        return lcm_2(v[0], v[1])
    }
    return lcm(v.pop(0), v)
}
