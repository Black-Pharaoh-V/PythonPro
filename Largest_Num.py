# Program to find the k-th largest Number in a 1D Array.
# TriTea@blackpharaoh

def main():
    arr = []
    n = int(input("Enter the size of the array."))

    print("Enter the elements of the array:")
    for i in range(n):
        arr.append(int(input(f"Element{i+1}")))   #taking and adding the elements using append.

    k= int(input("Enter the k-th largets number to search for:"))
    if k<=0:
        print("Invalid number!")
        return

    for i in range(n):
        for j in range(0,n-1):
             if arr[j] > arr[j+1]:   #sorting the array.
                 temp = arr[j]
                 arr[j]= arr[j+1]
                 arr[j+1]=arr[j]
                
    print(f"The {k} largest number is: {arr[n-k]}")

if __name__ == "__main__":
     main()