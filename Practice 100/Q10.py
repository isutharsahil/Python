a = int(input("Buying:-"))
b = int(input("Selling:-"))
if a > b:
    c = a-b
    print("Loss of",c)
elif a == b:
    print("None")
else:
    print("Loss")
