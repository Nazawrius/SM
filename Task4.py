from random import random

def monte_carlo_3d():
    N = 10000
    a = 3
    b = 27
    c = 3

    n = 0
    for _ in range(N):
        x = 2 * c * (random() - 0.5)
        y = 2 * c * (random() - 0.5)
        z = b * random()

        if (x*x + y*y)**a < z:
            n += 1
    
    print(f"Approximate volume: {4*c*c*b * n/N}")