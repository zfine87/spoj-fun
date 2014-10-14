import sys


def prime_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    try :    
        a = s.split()
        return [int(x) for x in a]
    except ValueError:
        return []

def prime_solve (r, w) :
    """
    r a reader
    w a writer
    """
    z = int(1000000000**.5)+1
    r.readline()
    while True :
        start_set = basic_sieve(z)
        l = prime_read(r)
        if not l :
            break
        if l[1] < z:
            for i in range (l[0], l[1]):
                if start_set[i]:
                    print(i)
        else: 
            sieve(l[0], l[1], start_set)
        print()

def subset_check(b, e) :
    global prime_list
    if min(l) <= b and max(l) >= e:
        return True
    else :
        return False


def prime_eval(n, d):
    for each in range(0, d):
        if each :
            print(n[each] + d)
    # if n % 2 == 0 or n % 3 == 0:
    #     unprime_set.add(n)
    #     return False
    # for i in range(5, int(n ** 0.5) + 1, 6):
    #     if n % i == 0 or n % (i + 2) == 0:
    #         unprime_set.add(n)
    #         return False
    # prime_set.add(n)
    # return True


def sieve(l, r, s):
    if l % 2:
        l -= 1
    if r % 2:
        r += 1
    count = 0
    p = []
    q = []
    # b = (r-l) // 10
    # if b < 10:
    #     b = r-l
    b = 100
    for i in range (3, int(r**.5)):
        if s[i]: 
            p.append(i)
    for each in p:
        q.append(int((-1/2*(l+1+each)) % each))
    for bl in range(l, r, b*2):
        #if not count % 2 and count > 0:
        bits = [1]*b
        for x in range(0, len(p)):
            for y in range(q[x], len(bits), p[x]):
                bits[y] = 0
        for i in range(0, len(bits)):
            if bits[i]:
                if (i*2+1+bl) >= l and (i*2+1+bl) <= r:
                    print(i*2+1+bl)
        #count += 1
        for i in range (0, len(q)):
            q[i] = (q[i] - b) % p[i]


def basic_sieve(n) :
    nums = [1] * n
    nums[1] = 0
    for i in range (2, int(n**.5)+1):
        if nums[i]:
            for j in range (i**2, n, i):
                nums[j] = False
    return nums


prime_solve(sys.stdin, sys.stdout)