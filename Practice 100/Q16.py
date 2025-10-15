a,b = map(float, input("temp° and humidity(%): ").split())
if a>=30 and b>=90:
    print("hot and humid")
elif a>=30 and b<90:
    print("hot")
elif a<30 and b>=90:
    print("cold and humid")
else:
    print("cold")