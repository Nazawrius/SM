from random import uniform

def monte_carlo_3d():
    N = 10000
    a = 3
    b = 27
    c = 3

    n = 0
    for _ in range(N):
        x = uniform(-c, c)
        y = uniform(-c, c)
        z = uniform(0, b)

        if (x*x + y*y)**a < z:
            n += 1
    
    print(f"Approximate volume: {4*c*c*b * n/N}")