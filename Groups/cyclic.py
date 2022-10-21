import math
import numpy as np
import pandas as pd

print("Welcome to LANG. What cyclic group would you like to view?\n")

choice = input()
choice = int(choice)

def elements(choice):
    elements = list(range(choice))
    print(f'\nOrder of Z{choice} is {len(elements)}\n')
    print(f'Elements of Z{choice}:\n')
    print(f'{elements}\n')

elements(choice)

print(f'\nGenerators of Z{choice}:\n')

def generators(choice): 
    print(euler_tot(choice))

def euler_tot(number):
    generators = []
    for i in range(0, number):
        if math.gcd(i, number) == 1:
            generators.append(i)
    return generators
 
generators(choice)

# Print out the lattice 

# Print out the matrix
