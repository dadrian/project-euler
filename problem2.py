def sumEvenFib(n):
	if n <= 1:
		return 0
	elif n == 2:
		return 2
	else:
		def fib(cur, prev, sum):
			if cur > n:
				return sum;
			if not cur % 2:
				sum += cur
			return fib(cur + prev, cur, sum)
		return fib(2, 1, 0)

print sumEvenFib(4000000)

