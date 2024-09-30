#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const long long maxN = 1000000;
vector<bool> primes_sieve(maxN + 1, true);
vector<long long> primes;

void populate_primes() {
    for (long long i = 2; i <= maxN; ++i) {
        if (primes_sieve[i]) {
            for (long long j = i * i; j <= maxN; j += i) {
                primes_sieve[j] = false;
            }
            primes.push_back(i);
        }
    }
}

vector<vector<long long>> get_total_divisors_range(long long a, long long b) {
    vector<vector<long long>> factors(b - a + 1);
    long long values[b - a + 1];

    for (long long i = 0; i < b - a + 1; ++i) {
        values[i] = a + i;
    }
    
    for (long long prime : primes) {
        if (prime > b) {
            break;
        }
        
        long long smallest = ((long long) (a / prime)) * prime;
        if (smallest < a) {
            smallest += prime;
        }
        
        while (smallest <= b) {
            long long idx = smallest - a;
            factors[idx].push_back(0);
            
            while (values[idx] % prime == 0) {
                factors[idx].back() += 1;
                values[idx] /= prime;
            }
                
            smallest += prime;
        }
    }

    for (long long i = 0; i < b - a + 1; ++i) {
        if (values[i] > 1) {
            factors[i].push_back(1);
        }
    }

    return factors;
}

void solve_case(long long a, long long b, const vector<vector<long long>>& factors) {
    long long d;
    cin >> d;
    long long s = 0;
    for (long long num = a; num <= b; num++) {
        if (num == d) {
            s += 1;
            continue;
        }
        
        long long divisors = 1;
        for (long long count : factors[num - a]) {
            divisors *= (count + 1);
            cout << num << " " << count << endl;
        }
        
        long long count_d = 0;
        long long temp_num = num;
        while (temp_num % d == 0) {
            count_d += 1;
            temp_num /= d;
        }
        s += divisors / (count_d + 1);
    }
    
    cout << s << endl;
}

int main() {
    long long total_cases, a, b;
    cin >> total_cases >> a >> b;
    populate_primes();
    vector<vector<long long>> factors = get_total_divisors_range(a, b);
    for (long long test_case = 0; test_case < total_cases; ++test_case) {
        solve_case(a, b, factors);
    }
    return 0;
}