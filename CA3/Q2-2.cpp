#include <iostream>
using namespace std;

// Function to calculate
// the hash of a string
long long polynomialRollingHash(
	string const& str)
{
	// P and M
	int p = 31;
	int m = 1e9 + 9;
	long long power_of_p = 1;
	long long hash_val = 0;

	// Loop to calculate the hash value
	// by iterating over the elements of string
	for (int i = 0; i < str.length(); i++) {
		hash_val
			= (hash_val
			+ (str[i] - 'a' + 1) * power_of_p)
			% m;
		power_of_p
			= (power_of_p * p) % m;
	}
	return hash_val;
}

/// Driver Code
int main()
{
	// Given strings
	string str1 = "aab";
	string str2 = "aac";

	cout << "Hash of '" << str1 << "' = "
		<< polynomialRollingHash(str1) << endl;
    
    cout << "Hash of s2 : '" << str2 << "' = "
		<< polynomialRollingHash(str2);
	cout << endl;
}
