a = str(input("Reverse a n-digit number: "))
print("ORIGINAL IS: ",a)
b = a[::-1]
print("REVERSED IS: ",b)
if b == a[::-1]:
    print(True)
else:
    print(False)