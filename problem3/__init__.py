import math

def primes(n):
	table = [True]*(n+1)
	table[0] = False
	table[1] = False

	for i in xrange(2, n):
		if table[i]:
			yield i
			for j in xrange(2*i, n, i):
				table[j] = False

def multiples(n):
	for i in xrange(1, (n/2)):
		if n % i == 0:
			yield i

def prime_multiples(n):
	for prime in primes(int(math.sqrt(n)+1)):
		if n % prime == 0:
			yield prime

print max(prime_multiples(600851475143))