#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

import sys

MAX = 100

def calculate_sum(arr):
    result = 0
    for num in arr:
        result += num
    return result

def main():
    try:
        n = int(input("Enter the number of elements (1-100): "))
        if not 1 <= n <= MAX:
            print("Invalid input. Please provide a number ranging from 1 to 100.")
            sys.exit(1)

        arr = []

        print(f"Enter {n} integers:")
        for _ in range(n):
            try:
                arr.append(int(input()))
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                sys.exit(1)

        total = calculate_sum(arr)

        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()