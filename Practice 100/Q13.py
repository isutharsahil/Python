a = int(input("A number: "))
if a % 3 == 0 and a % 6 == 0:
    print("yes,this no is divisible by 3 and 6 both: ")
elif a % 3 == 0:
    print("only divisible by 3")
else:
    print("no its not divisible by 6 or 3 ")