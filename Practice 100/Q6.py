def even_odd():
    try:
        a = int(input("Enter a number to check if its even or odd : "))
        if a % 2 == 0:
            print(f"{a} is even")
        else:
            print(f"{a} is odd")
    except:
        print("We accept only intigers. xD")

even_odd()