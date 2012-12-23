def sumMultiples(n):
	sum = 0
	for i in range(0, n):
		if not i % 3 or not i % 5:
			sum += i;
	return sum;
print sumMultiples(10);
print sumMultiples(1000);
