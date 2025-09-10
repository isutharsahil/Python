HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("history clear")

def save_history(equation, result):
    file = open(HISTORY_FILE,"a")
    file.write(equation + "=" + str(result) + '\n')
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print(" invalid input use 23 + 24 foramt")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    # Perform calculation

    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot perform floor division by zero.")
            return
        result = num1/num2
    elif op == "%":
        if num2 == 0:
            print("Error: Cannot modulo by zero.")
            return
        result = num1%num2
    elif op == "//":
        if num2 == 0:
            print("Error: Cannot perform floor division by zero.")
            return
        result = num1//num2
    else:
        print("Please choose wisely")
        return

    if result == int(result):
        result = int(result)
    print("result: ", result)
    save_history(user_input,result)


def main():
    print("Simple Calculator. (Type History,Clear or Exit)")
    while True:
        user_input = input("Enter calculation ('+' '-' * '/' '//' ) eg:  -->") 
        if user_input.lower == "exit":
            print("Goodbye!")
            break
        elif user_input.lower == "history":
            show_history()
        elif user_input.lower == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
        