# Program to print Pascal's Triangle
# TriTea@blackpharaoh

def pascal(n):
    for i in range(n):
        print(" " * ((n-i)*2), end="") # print spaces for center alignment
        value = 1
        for j in range(i+1):
            print(value, end="  ")
            value = value * (i - j) // (j + 1)
        print()

def main():
    n = int(input("Enter the number of lines for Pascal's Triangle: "))
    pascal(n)

if __name__ == "__main__":
      main()
