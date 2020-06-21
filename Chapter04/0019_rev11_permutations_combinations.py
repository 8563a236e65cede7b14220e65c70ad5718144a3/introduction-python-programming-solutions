'''
Review Question 11
Use functions to find nPr and nCr where nPr is a permutation
and nCr is a combination.

nPr = n! / (n-r)!
nCr = n! / r!(n-r)!
'''


def factorial(n):
    if n == 0:
        return 1

    res = 1
    while n > 1:
        res *= n
        n -= 1

    return res


def npr(n, r):
    return factorial(n) / factorial(n - r)


def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def main():
    n = int(input("Enter n\n"))
    r = int(input("Enter r\n"))

    if r > n:
        print("r needs to be smaller than n")
        return

    print(f"nPr = {npr(n, r)}, nCr = {ncr(n, r)}")


if __name__ == "__main__":
    main()


