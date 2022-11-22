import math
def f(n):
    factors = []    # create a list
    for i in range(1, int(math.sqrt(n))+1): #check if it is a factor
        if n%i == 0:
            x = True
            for j in range(1, int(math.sqrt(i))+1): #check if factor is prime
                if i%j == 0:
                    x = False
                x = True
            if x:
                factors.append(i)
    return max(factors)

print(f(600851475143))