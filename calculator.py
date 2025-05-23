def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def main():
    print("Basic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice")
            return

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()