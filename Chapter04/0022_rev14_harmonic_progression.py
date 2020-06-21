"""
Review Question 14
Print harmonic progression and sum up to N terms using
functions

"""


def harmonic(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1 / i
        if i == n:
            print(f"1/{i}\n")
        else:
            print(f"1/{i} + ", end="")
    return sum


def main():
    n = int(input("Enter number of terms in series"))
    sum = harmonic(n)
    print(f"The sum is {sum}")

if __name__ == "__main__":
    main()