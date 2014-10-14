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

def prime_write(w, l) :
    for i in range(0, len(l)-1):
        if l[i] == "":
            i += 1
        w.write(l[i] + "\n")


def prime_solve (r, w) :
    """
    r a reader
    w a writer
    """
    count = 0
    z = int(1000000000**.5)+1
    num_tests = int(r.readline())
    while count <= num_tests :
        start_set = basic_sieve(z)
        l = prime_read(r)
        if not l :
            break
        if l[1] <= z:
            for i in range (l[0], l[1]+1):
                if start_set[i]:
                    w.write(str(i) + "\n")
        elif l[0] <= z:
            for i in range (l[0], z):
                if start_set[i]:
                    w.write(str(i) + "\n")
            sieve(z, l[1], start_set, w)            
        else:
            sieve(l[0], l[1], start_set, w)
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


def sieve(l, r, s, w):
    if l % 2:
        l -= 1
    if r % 2:
        r += 1
    count = 0
    p = []
    q = []
    b = 100
    for i in range (3, int(r**.5)):
        if s[i]: 
            p.append(i)
    for each in p:
        q.append(int((-1/2*(l+1+each)) % each))
    for bl in range(l, r, b*2):
        bits = [1]*b
        for x in range(0, len(p)):
            for y in range(q[x], len(bits), p[x]):
                bits[y] = 0
        for i in range(0, len(bits)):
            if bits[i]:
                if (i*2+1+bl) >= l and (i*2+1+bl) <= r:
                    w.write(str(i*2+1+bl) + "\n")
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