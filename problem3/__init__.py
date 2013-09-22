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

def prime_factors(n):
	for i in xrange(2, int(math.sqrt(n))+1):
		if n % i == 0:
			yield i
			while n % i == 0:
				n = n / i
		if n == 1:
			return

if __name__ == '__main__':
	print max(prime_factors(600851475143))

	