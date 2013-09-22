
def mul3and5(n):
	i = 3
	while i < n:
		if i % 3 == 0 or i % 5 == 0:
			yield i
		i = i + 1

if __name__ == '__main__':
	print sum(mul3and5(10000))
