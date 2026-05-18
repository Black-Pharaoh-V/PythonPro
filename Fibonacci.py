# Program to print Fibonacci series upto a significant terms.
# TriTea@blackpharaoh

def fibonacci(n):  #Function to calculate fibonacci series using recursion.
     if n<=1:
          return n
     else:
          return fibonacci(n-1)+fibonacci(n-2)
     
def main():
     num = int(input("Enter the number of terms:"))
     if num <= 0:
          print("Invalid input!")
          return
     print(f"Series upto {num} terms is:")
     for i in range(num):
          print(f"{fibonacci(i)} ")
          
if __name__ == "__main__":
    main()