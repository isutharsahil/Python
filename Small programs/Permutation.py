def permutation(n,r):
    try:
        n = int(n); r = int(r)
        nr = n-r
        if (n<r):
            print("not possible n is greater than r")
            return
        else:
                f1 = 1
                for N in range(1,n+1):
                    f1 =f1*N
                f2 = 1    
                for R in range(1,nr+1):
                    f2=f2*R
                print("permutation: ",f1//f2)

        print()
    except:
        print("input error")            

permutation(12,2)