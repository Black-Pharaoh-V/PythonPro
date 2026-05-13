# Program to check Armstrong numbers and also print all Armstrong numbers in a given range.
# TriTea@blackpharaoh

def isarmstrong(n):
    s = 0
    temp = n
    p = len(str(n)) 
    while temp > 0:
        r = temp % 10
        s += r ** p
        temp //= 10
    
    # Return True if it's an Armstrong number, False otherwise
    return s == n

def armstrongrange(f, l):
    for i in range(f, l + 1):
        # Call the logic function here
        if isarmstrong(i):
            print(f"{i}", end=", ")
    print() 

def main():
    ct = 1
    while ct == 1:
        print("\nEnter your choice please: \n 1. Verify a Number \n 2. Find a given range. \n 3. Exit")
        ch = int(input())
        
        if ch == 1:
            print("Enter the number to verify: ")
            num = int(input())
            # Use the return value to decide what to print
            if isarmstrong(num):
                print(f"{num} is an Armstrong number")
            else:
                print(f"{num} is not an Armstrong number")
            
            print("Press 1 to continue or 0 to exit:")
            ct = int(input())
            
        elif ch == 2:
            print("Enter the range to find armstrong numbers: ")
            f = int(input("From: "))
            l = int(input("To: "))
            if f > l:
                print("Invalid range")
            else:
                armstrongrange(f, l)
            
            print("Press 1 to continue or 0 to exit:")
            ct = int(input())
            
        elif ch == 3:
            ct = 0
        else:
            print("Invalid choice")
            print("Press 1 to continue or 0 to exit:")
            ct = int(input())

if __name__ == "__main__":
    main()