# Fibonacci Sequence
# Enter a number and have the program generate the Fibonacci sequence to
# that number or to the Nth number.


def get_fibonacci_seq(n):
    res = [1,1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res[:n]


if __name__ == "__main__":
    try:
        n = int(raw_input("How many numbers in the sequence? "))
        seq = get_fibonacci_seq(n)
        print seq
    except:
        print "Invalid input"