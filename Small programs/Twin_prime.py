def twin_prime(a, b):
    try:
        a = int(a) ; b = int(b)
        if a<=1 or b<=1:
            print("nopes ❌")
        else:
            prime_a = True
            for i in range(2,a):
                if a % i == 0:
                    prime_a = False
                    break
            prime_b = True
            for j in range(2,b):
                if b % j == 0:
                    prime_b = False
                    break               
            if prime_a and prime_b and abs(a-b) == 2:
                print("Twin Prime ✅")
            else:
                print("Not Twin Prime ❌")
    except:
        print("input error")

twin_prime(5, 7)