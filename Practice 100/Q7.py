def leap_year():
    try:
        year = int(input("Fill Year: "))
        if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
            print(f"{year} is a leap year.")
        else:
            print("Not a leap year")
            

    except: 
        print("numbers only")    
leap_year()

# year 4 and 400 devide hojana chiye 
# year 100 % se devide nhi hona chiye