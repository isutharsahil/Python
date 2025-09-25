a = int(input("start: "))
b = int(input("ends: "))
if a > b and a < 1:
    print("sahi se value dalo")
else:
    for number in range(a, b+1):
        for i in range(2, number):
            if number % i == 0 :
                break
        else:
            print("prime num = ", number)