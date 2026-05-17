# Program to convert an integer to binary and vice versa
# TriTea@blackpharaoh

def int_to_bin(n):
    binary = 0
    power = 1
    while n> 0:
        rem = n%2
        binary += rem*power
        power *= 10
        n //= 2 # // is used for floor division
    return binary

def bin_to_int(binary):
    n=0
    power = 1
    while binary > 0:
        rem = binary % 10
        n+= rem*power
        power *= 2
        binary //= 10
    return n

def main():
     choice = 1
     while choice == 1:
         print("1. Integer to Binary\n2. Binary to Integer\nEnter your choice: \n")
         choice = int(input())
         match choice:
             case 1:
                 n = int(input("Enter a integer: "))
                 print(f"Binary equivalent is: {int_to_bin(n)}")
                 break
             case 2:
                 binary = int(input("Enter a binary number: "))
                 print(f"Integer equivalent is: {bin_to_int(binary)}")
                 break
             case _:
                 print("Invalid choice! Please try again.")
                 break
             
         print("Do you want to continue? (Press 1 for Yes, 0 for No)")
         choice = int(input()) # To check if the user wants to continue or not  

     if __name__ == "__main__":
         main()

