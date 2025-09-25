try:    
    a, b, c = map(int, input("input 3 numbers eg {60 60 60} : ").split())
    if a>0 and b>0 and c>0 and a+b+c == 180:
        print("it does 😎")
    else:
        print("it does not 😣")
except:
    print("invalid input 😶‍🌫️")