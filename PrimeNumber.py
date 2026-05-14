#Program to check whether a number is prime or not, also to print the prime number in a given range.
#TriTea@blackpharaoh

import math
def isPrime(n):  #Function to check if a number is prime or not.
    if n<=1:
         return False
    for i in range(2,math.isqrt(n)+1): # isqrt is used to get the integer value of square root rather than floating point value.
         if n%i == 0:
              return False #not prime
    return True #prime

def RangePrime(f, l):
        for i in range(f, l+1):
            if isPrime(i):
                print(i, end=" ") #print the prime numbers in the given range.

def main():
     choice = 1
     while choice == 1:
          choice = int(input("1 to check if a number is prime or not. \n2 to print prime numbers in a given range \nEnter Your Choice: "))
          match choice:
               case 1:
                    n = int(input("Enter a number: "))
                    if isPrime(n):
                         print(f"{n} is a prime number.")
                    else:
                         print(f"{n} is not a prime number.")
                    break
               case 2:
                    f = int(input("Enter the first number of the range: "))
                    l = int(input("Enter the last number of the range: "))
                    if f > l:
                         print("Invalid range. First number should be less than or equal to last number.")
                         break
                    print("Prime numbers in the given range are: ")
                    RangePrime(f, l)
                    break
               case _:
                    print("Invalid choice. Please enter 1 or 2.")
                    break
            
          print("Do you want to continue? (1 for Yes, 0 for No): ")
          choice = int(input())

if __name__ == "__main__":
     main()

    
