# Prime Factorization
# Have the user enter a number and find all Prime Factors (if there are any) and display them.

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def get_prime_factors(n):
    res = []
    for i in range(1, n/2+1):
        if (n % i == 0) and is_prime(i):
            res.append(i)
            
    if is_prime(n):
        res.append(n)

    return res

if __name__ == "__main__":
    try:
        n = int(raw_input("Pick a number: "))
        pf = get_prime_factors(n)
        print pf
    except:
        print "Invalid input"
