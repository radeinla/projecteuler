
import math

def fib(n):
	a, b = 0, 1

	while a < n:
		yield a
		b = a + b
		a = b - a

def prime_factors(n):
	for i in xrange(2, int(math.sqrt(n))+1):
		if n % i == 0:
			yield i
			while n % i == 0:
				n = n / i
		if n == 1:
			return

def is_palindrome(n):
	i = int(math.log(n)/math.log(10))
	j = 10**i
	# print j
	while i > 0:
		x = n / j
		if x != n % 10:
			return False
		else:
			n -= x * j + x
		n = n / 10
		j = j / 100
		i = i - 2
	return True

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
