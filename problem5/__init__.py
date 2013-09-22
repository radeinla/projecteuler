

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


if __name__ == '__main__':
	product = 1
	for i in xrange(2, 21):
		product = (product * i) / gcd(product, i)
	print product
	
