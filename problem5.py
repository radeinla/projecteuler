from lib import gcd

if __name__ == '__main__':
	product = 1
	for i in xrange(2, 21):
		product = (product * i) / gcd(product, i)
	print product
	
