import math

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

def three_digit_palindromes():
	for i in xrange(100, 1000):
		for j in xrange(100, 1000):
			if is_palindrome(i*j):
				yield i*j

if __name__ == '__main__':
	# print(list(three_digit_palindromes()))
	print(max(three_digit_palindromes()))

