#Write a program that will take three digits from the user and add the square of each digit.

a = (input("enter three digit no: "))

result = sum(int(digit)**3 for digit in a)          #loop methord
print(f" sum of squares of digit {result}")




''' 
                #for basic understanding
a1 = int(a[0])                                      
a2 = int(a[1])  #manual mapping
a3 = int(a[2])

print(f"{a1**2+a2**2+a3**2}")

'''               

