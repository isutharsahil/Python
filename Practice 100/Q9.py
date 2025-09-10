a = int(input("1-"))
b = int(input("2-"))
c = int(input("3-"))

# x = a+b > c and a+c > b and b+c > a
# if x:
#     print("Possible")
# else:
#     print("Not Possible")

if a+b+c== 180:
    print("Possible")
else:
    print("Not Possible")