

def sum_square_difference(n):
	total = 0
	for i in xrange(1, n+1):
		for j in xrange(i+1, n+1):
			print i, j
			total = total + i*j
	return total * 2

if __name__ == '__main__':
	print sum_square_difference(100)

# a^2 + b^2 + c^2 + d^2 + e^2

# (a + b + c + d + e)^2
# (a + (b + c + d + e))^2
# a^2 + 2*a*(b + c + d + e) + (b + c  + d + e)^2
# a^2 + 2*a*b + 2*a*c + 2*a*d + 2*a*e + b^2 + 2*b*c + 2*b*d + 2*b*e + c^2 + 2*c*d + 2*c*e + d^2 + 2*d*e + e^2

# 2*a*b + 2*a*c + 2*a*d + 2*a*e + 2*b*c + 2*b*d + 2*b*e + 2*c*d + 2*c*e + 2*d*e
# 2(a*b + a*c + a*d + a*e + b*c + b*d + b*e + c*d + c*e + d*e)

# you suck at linear algebra..... =)))
# 0, 0, 0, 1 = 0
# 1, 1, 1, 1 = 1
# 8, 4, 2, 1 = 5
# 27, 9, 3, 1 = 14
