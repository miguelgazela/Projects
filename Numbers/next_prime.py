import math


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    i = num + 1
    while True:
        if is_prime(i):
            return i
        i += 1

if __name__ == "__main__":
    print "Press enter to continue, done to stop"

    i = 2
    while True:
        print i,
        user_input = raw_input()
        if user_input == 'done':
            break
        i = get_next_prime(i)
