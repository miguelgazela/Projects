# Factorial Finder
# The Factorial of a positive integer, n, is defined as the product of the
# sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as
# being 1. Solve this using both loops and recursion.

def factorial(n):
    result = 1

    if n == 0:
        return result

    while n > 0:
        result *= n
        n -= 1

    return result


def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)


def main():
    n = 5
    result = factorial_rec(n)
    print result
    result = factorial(n)
    print result


if __name__ == "__main__":
    main()