from random import randint, getrandbits

import numpy as np
import matplotlib.pyplot as plt

def coin_tosses():
    N = int(input("Enter a number of coin tosses: "))
    s = bin(getrandbits(N))[2:]
    ones = s.count('1')
    zeros = s.count('0')
    print(f"Number of heads: {ones}, percentage: {ones/N}")
    print(f"Number of tails: {zeros}, percentage: {zeros/N}")

def single_dice_rolls():
    N = int(input("Enter a number of dice rolls: "))
    l = [randint(1, 6) for _ in range(N)]
    print(f"Mean: {np.mean(l)}")
    print(f"Variance: {np.var(l)}")
    print(f"Standart deviation: {np.std(l)}")
    
    plt.hist(l, bins=np.arange(0.5, 7.5, 1), rwidth=0.7)
    plt.show()

def double_dice_rolls():
    N = int(input("Enter a number of dice rolls: "))
    l = [randint(1, 6)+randint(1,6) for _ in range(N)]
    print(f"Mean: {np.mean(l)}")
    print(f"Variance: {np.var(l)}")
    print(f"Standart deviation: {np.std(l)}")
    
    plt.hist(l, bins=np.arange(1.5, 13.5, 1), rwidth=0.7)
    plt.show()