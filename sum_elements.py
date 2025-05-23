# This program calculates the sum of user-provided integers with basic error handling.

import sys

MAX = 100

def calculate_sum(arr):
    return sum(arr)

def main():
    try:
        n = int(input("Enter the number of elements (1-100): "))
        if not 1 <= n <= MAX:
            print("Invalid input. Please provide a number ranging from 1 to 100.")
            sys.exit(1)

        arr = []
        print(f"Enter {n} integers:")

        for i in range(n):
            while True:
                try:
                    value = int(input(f"Element {i+1}: "))
                    arr.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()