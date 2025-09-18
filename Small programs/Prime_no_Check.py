def prime(a):
    try:
        a = int(a)
        if a <= 1:
            print("not prime")
        else:
            for i in range(2,a):
                if a % i == 0:
                    print("not prime")
                    break
            else:
                print("prime")
    except:
        print("input error")

def main():
    print("Enter no to check if its prime no or not.")
    print("Type exit to stop")
    
    while True:
        a = input("Enter Here: ")
        if a == "exit":
            print('bye')
            break
        else:
            prime(a)

main()