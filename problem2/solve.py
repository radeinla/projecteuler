
def even_fib(n):
	a, b = 0, 1

	while a < n:
		if a % 2 == 0:
			yield a
		b = a + b
		a = b - a

print sum(even_fib(4000000))
