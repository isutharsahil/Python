# program to find simple interest

p = float(input("P :")) #price
r = float(input("R% :"))  #Interest rate
t = float(input("T :"))  #Time
For = p*r*t/100
print(f"total amount after {t} year will be {For+p}")
