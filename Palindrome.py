#Program to check whether the given number is palindrome or not, and print the palindrome in a given range.
#TriTea@blackpharaoh

def isPalindrome(num):
    temp = num
    rev = 0
    while temp > 0:
        r = temp % 10
        rev = rev * 10 + r
        temp = temp // 10 #because we are working with integers, we can use floor division to get the quotient without the remainder
    return rev == num

def RangePalindrome(start, end):
    print(f"Palindrome numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if isPalindrome(num):
            print(num, end=" ")
    print() #for a new line after printing all palindrome numbers

def main():
    Choice = 1 
    while choice == 1:
        print("1. Check if a number is a palindrome\n2. Print palindrome numbers in a range\nEnter your choice: ", end="")
        choice = int(input())
        if choice == 1:
         num = int(input("Enter a number: "))
         if isPalindrome(num):
             print(f"{num} is a palindrome number.")
         else:
             print(f"{num} is not a palindrome number.")
         print("Do you want to continue? (1 for Yes, 0 for No): ", end="")
         choice = int(input())
         break
        elif choice == 2:
         start = int(input("Enter the starting number: "))
         end = int(input("Enter the ending number: "))
         if start > end:
             print("Invalid range. Starting number should be less than or equal to ending number.")
             continue
         RangePalindrome(start, end)
         print("Do you want to continue? (1 for Yes, 0 for No): ", end="")
         choice = int(input())
         break
        else:
         print("Invalid choice. Please enter 1 or 2.")
         choice = 1
         break
        
if __name__ == "__main__":
    main()
