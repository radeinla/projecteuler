from lib import is_palindrome

def three_digit_palindromes():
	for i in xrange(100, 1000):
		for j in xrange(100, 1000):
			if is_palindrome(i*j):
				yield i*j

if __name__ == '__main__':
	print(max(three_digit_palindromes()))

