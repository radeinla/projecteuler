
def fib(n):
	a, b = 0, 1

	while a < n:
		yield a
		b = a + b
		a = b - a


def even_fib(n):
	for f in fib(n):
		if f % 2 == 0:
			yield f
			
print sum(even_fib(4000000))
