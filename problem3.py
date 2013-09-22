
from lib import prime_factors

def multiples(n):
	for i in xrange(1, (n/2)):
		if n % i == 0:
			yield i

if __name__ == '__main__':
	print(max(prime_factors(600851475143)))

