def permutation_fast(n, r):
    try:
        n=int(n) ; r=int(r)
        
        if n<r:

            print('not possible')
            return
        
        else:
            result = 1
            for factorial in range(n,n-r,-1):
                result *= factorial
            
            print("permutation:", result)
    
    except:
        print("input error")

permutation_fast(5,3)
