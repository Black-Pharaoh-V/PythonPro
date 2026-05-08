#Program to check if a number is an Armstrong number or not and to find all the armstrong number in a given range
#TriTea@blackpharaoh

def isarmstrong(n):
    s = 0
    temp= n
    while temp >0:
        r= temp % 10
        s += r*r*r
        temp //= 10
    if s == n:
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")

def armstrongrange(f,l):
    for i in range(f,l+1):
        s = 0
        temp= i
        while temp >0:
            r= temp % 10
            s += r*r*r
            temp //= 10
        if s == i:
            print(f"{i},  ")  

def main():
    print("Enter your choice please: \n 1. Verify a Number \n 2.Find a given range.")
    ch = int(input())
    ct = 1
    while ct == 1:
     if ch == 1:
         print("Enter the number to verify: ")
         num = int(input())
         isarmstrong(num)
         print("Press 1 to continue or 0 to exit:")
         ct = int(input())
     elif ch == 2:
         print("Enter the range to find armstrong numbers: ")
         f = int(input("From: "))
         l = int(input("To: "))
         if f>l:
             print("Invalid range")
             print("Press 1 to continue or 0 to exit:")
             ct = int(input())
             continue
         armstrongrange(f,l)
         print("Press 1 to continue or 0 to exit:")
         ct = int(input())
     else:
         print("Invalid choice")
         print("Press 1 to continue or 0 to exit:")
         ct = int(input())

if __name__ == "__main__":
    main()
    