from random import random

def monte_carlo_2d():
    N = 10000
    a = 6
    b = 4

    n = 0
    for _ in range(N):
        x = 12 * (random() - 0.5)
        y = 12 * (random() - 0.5)

        if x*x/(a*a) + y*y/(b*b) <= 1 and x*x/(b*b) + y*y/(a*a) <= 1:
            n += 1
    
    print(f"Approximate area: {a*a * n/N}")