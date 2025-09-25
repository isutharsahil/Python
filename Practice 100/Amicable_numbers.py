def sum_of_divisible(n):
    total=0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total


def amicable(limit):
    try:
        for a in range(2, limit+1):
            b= sum_of_divisible(a)                  # ex: a = 220  -> sum of divisible -> B = 284
            if b!=a and b <= limit:
                if sum_of_divisible(b) == a:        # 284 ke devisible ka sum has to be 220
                    if a<b:                         # then only it will be amicable
                        print(f"{a}, {b} are amicable numbers.")   

    except:
        print("input error")

amicable(1000)