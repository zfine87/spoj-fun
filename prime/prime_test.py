import sys


def prime_check(r):
	while True:
		s = r.readline()
		if s == "":
			print("EOF")
			break
		if s == '\n':
			print("skip")
		else :
			if is_prime(int(s)):
				print("good     " + s)
			else :
				print(int(s))
				break

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

prime_check(sys.stdin)