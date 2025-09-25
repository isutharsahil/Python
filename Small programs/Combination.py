def combination(n, r):
    try:
        if n < r:
            return False
        else:
            result = 1
            for i in range(n, n-r, -1):
                result *= i
            
            result_2 = 1
            for j in range(r, 1, -1):
                result_2 *= j

            print(f"{result // result_2} is your combination")

    except:
        print("input error")

combination(5,2)