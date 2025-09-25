def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
            break
    return True

for number in range(2,1000):
    if prime(number) and prime(number+2) and abs(number-number+2) == 2:
        print(number, number+2)