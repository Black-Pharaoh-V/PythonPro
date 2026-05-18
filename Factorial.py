# Program to find the factorial of a number using recursion and also print them in a given range.
# TriTea@blackpharaoh

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

def RangeFactorials(start, end):
    print(f"Factorials from {start} to {end}:")
    for i in range(start, end + 1):
        print(f"{i}! = {factorial(i)}")
        
def main():
    choice = 1
    while choice == 1:
        print("1. Calculate factorial of a number\n2. Calculate factorials in a range\nEnter your choice:\n")
        choice = int(input())
        if choice == 1:
            num = int(input("Enter a number:"))
            if num < 0:
                    print("Factorial is not defined for negative numbers.")
            else:
                    print(f"Factorial of {num} is {factorial(num)}")
            print("Do you want to continue? (1 for yes, 0 for no)")
            choice = int(input())
        elif choice == 2:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            if start > end or start < 0:
                print("Invalid range. Please enter a valid range where start is less than or equal to end and both are non-negative.")
            else:
              RangeFactorials(start, end)
            print("Do you want to continue? (1 for yes, 0 for no)")
            choice = int(input())
        else:
            print("Invalid choice. Please enter 1 or 2.")
            print("Do you want to continue? (1 for yes, 0 for no)")
            choice = int(input())

if __name__ == "__main__":
    main()