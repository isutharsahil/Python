def age_comparison():
    try:
        a, b, c = map(int, input("Enter age in {20 22 32} format: ").split())
        print("Your input is correct!")

        if (a>=b and a>=c):
            print(f"First one is the oldest : {a}")
        elif (b>=a and b>=c):
            print(f"Second one is the oldest : {b}")
        else:
            print(f"Third one is the oldest : {c}")
    except ValueError:
        print("Your input is incorrect! :(")

age_comparison()