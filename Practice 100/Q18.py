# narcissist and armstrong no are same mathematical concept only name is different.


a = (input("enter three digit no: "))
result = sum(int(digit)**3 for digit in a)

if result == int(a):
    print(f" sum of squares of digit {result}")
else:
    print("its not")