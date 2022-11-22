def isdivisiblebyall(n):
    for i in range(11, 21):
        if n % i != 0:
            return False
    return True

no = 2520
while not isdivisiblebyall(no):
    ## if number is not divisible by range of 11 to 20 the value of 'no' will be incremented by 2520       
    no+=2520
print(no)