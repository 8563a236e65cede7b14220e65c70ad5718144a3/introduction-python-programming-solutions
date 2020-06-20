'''
Program 4.9
Demonstrate the Use of Default Parameters
'''

def work_area(prompt, domain="Data Analytics"):
    print(f"{prompt} {domain}")

def main():
    work_area("Sam works in")
    work_area("Alice has interest in", "Internet of Things")
    work_area("Sam works in")

if __name__ == "__main__":
    main()
