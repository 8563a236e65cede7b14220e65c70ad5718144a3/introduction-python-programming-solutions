'''
Program 4.10
Demonstrate Keyword Arguments
'''

def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print(f"This parrot wouldn't {action}, if you put {voltage}, volts through it.")
    print(f"Lovely plumage, the {type}")
    print(f"It's {state}!!!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action="VOOOOOM")
parrot("a thousand", state="pushing up the daisies")

