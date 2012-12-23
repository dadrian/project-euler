# Let's do a quasi simple brute force.
# 
# First, we'll calculate all the primes up to (n/3). Then we'll loop through them
# top down to find the largest prime factor.
#

def sieve(n):
	marks = [False for x in range(0,n+1)]
	for i in range(2, n+1):
		if marks[i]:
			continue
		difference = i;
		divisor = 2*i;
		while divisor < n+1:
			marks[divisor] = True
			divisor += difference
	primes = [i for i in filter(lambda f: not marks[f], range(n, 0, -1))]
	return primes

def largestFactor(n):
	primes = sieve(n/3)
	for i in primes:
		if not n % i:
			return i
	return n

print largestFactor(57)
print largestFactor(20000001)
#print largestFactor(600851475143)
