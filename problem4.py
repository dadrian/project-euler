def checkPalindrome(s):
	front = 0
	back = len(s) - 1
	while front < back:
		if s[front] != s[back]:
			return False
		front += 1
		back -= 1
	return True

def findLargestPalindrome(lower, upper):
	big = 0;
	m = upper
	n = upper
	while m >= lower:
		while n >= lower:
			p = m*n
			if checkPalindrome(str(p)):
				if p > big:
					print m,n,p
					big = p
			n -= 1
		n = upper
		m -= 1
	return big

print findLargestPalindrome(100, 999)
