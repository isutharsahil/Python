r = int(input("Radius in cm: "))
h = int(input("heighti in cm: "))
v = (3.14*r*r*h) # it will give volume of cylinder in cm3
liter = v/1000   # kitna liters isme aa skta hai cm3 into cost of milk per ltr 
cost = liter*40   # (kitne rupe ka doodh isme aajaega)
print(f"Volume of a cylinder is {v}cm^3")
print(f"cost of milk is {cost}")
