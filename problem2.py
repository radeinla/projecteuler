from lib import fib

def even_fib(n):
	for f in fib(n):
		if f % 2 == 0:
			yield f


if __name__ == '__main__':		
	print sum(even_fib(4000000))
