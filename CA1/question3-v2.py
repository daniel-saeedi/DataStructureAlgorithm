""" Calculates prime numbers from 1 to sqrt(n) """
# from itertools import compress
#n = 10**5
# def primes(n):
#     """ Returns  a list of primes < n for n > 2 """
#     sieve = bytearray([True]) * (n//2)
#     for i in range(3,int(n**0.5)+1,2):
#         if sieve[i//2]:
#             sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
#     return [2,*compress(range(3,n,2), sieve[1:])]
# primeslist = primes(int(n**0.5)+1)
""" For time efficiency I calculated this before"""
primeslist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]

numbers_set = list()

def insert_divisors(n, counter_dict):
  i = 1
  # Note that this loop runs till square root 
  while i <= n**(1/2): 
    if (n % i == 0) : 
      if (n / i == i):
        counter_dict[i] = counter_dict.get(i, 0) + 1
      else :
        counter_dict[i] = counter_dict.get(i, 0) + 1
        counter_dict[n//i] = counter_dict.get(n//i, 0) + 1
    i = i + 1

""" Returns a list of the prime factorization of n """
def factorization(n, primeslist):
    pf = []
    for p in primeslist:
      if p*p > n : break
      count = 0
      while not n % p:
        n //= p
        count += 1
      if count > 0: pf.append((p, count))
    if n > 1: pf.append((n, 1))
    return pf

""" Returns an unsorted list of the divisors of n """
def insert_divisors(n, primeslist, counter_dict):
    divs = [1]
    for p, e in factorization(n, primeslist):
        divs += [x*p**k for k in range(1,e+1) for x in divs]
    for div in divs:
      counter_dict[div] = counter_dict.get(div, 0) + 1


def count_divisors(query, counter_dict):
  if query not in counter_dict:
    return 0
  return counter_dict[query]

i = 1
counter_dict = {}
max_lines = int(input())
while i <= max_lines :
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a == 1 :
        numbers_set = insert_divisors(b, primeslist, counter_dict)
        # print('counter_dict', counter_dict)
    else :
        print(count_divisors(b, counter_dict))
    i += 1