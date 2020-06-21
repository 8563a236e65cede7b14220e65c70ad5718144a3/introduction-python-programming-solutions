"""
Review Question 15
Program to:
    a) convert milliseconds to hours, minutes, and seconds
    b) computer sales commission, given the sales amount and
       the commission rate
    c) convert celsius to fahrenheit
    d) compute the monthly payment, given the loan amount,
       number of years and the annual interest rate



"""


def ms_to_hms():
    milli = float(input("Enter number of milliseconds to convert\n"))
    if milli < 0:
        print("Please enter positive time value")
        return

    seconds = milli / 1000
    minutes = seconds / 60
    hours = minutes / 60

    minutes = (hours - int(hours)) * 60
    seconds = (minutes - int(minutes)) * 60

    print(f"{milli} ms = ")
    print(f"{int(hours)} hours")
    print(f"{int(minutes)} minutes")
    print(f"{seconds} seconds")


def commission():
    sales = float(input("Enter the sales amount\n"))
    rate = float(input("Enter commission rate as a decimal\n"))

    if sales < 0 or rate < 0:
        print("Please enter positive sales or rate values")
        return

    print(f"R{sales} * {rate*100}% = R{sales * rate}")


def cel_to_far():
    celsius = float(input("Enter the temperature in celsius\n"))
    print(f"{celsius}C = {celsius * 9/5 + 32}F")


def payment():
    #x = L * [(1+i)^(1/12)-1] / [1-v^n]
    loan = float(input("Enter the loan amount\n"))
    years = float(input("Enter the number of years\n"))
    interest = float(input("Enter the interest rate as a decimal\n"))

    if loan < 0 or years < 0 or interest < 0:
        print("Please enter positive values for all inputs")
        return

    payment = loan * (pow(1+interest, 1/12) - 1) / (1 - pow(1+interest, -years))

    print(f"The monthly repayment is R{payment}")


def main():
    while True:
        command = input("What do you want to calculate?\n(time, commission, temperature, monthly payment, done)\n")

        if command == "done":
            break
        else:
            if command == "time":
                ms_to_hms()
            elif command == "commission":
                commission()
            elif command == "temperature":
                cel_to_far()
            elif command == "monthly payment":
                payment()
            else:
                print("Invalid command")


if __name__ == "__main__":
    main()

