cost = int(input("Cost price: "))
sell = int(input("selling price: "))
if cost > sell:
    c = cost-sell
    print("Loss of",c)
else:
    d = sell-cost    
    print("Profit",d)
