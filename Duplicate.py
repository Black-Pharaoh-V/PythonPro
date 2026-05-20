# Program to print the duplicate number in a single dimension array.
# TriTea@blackpharaoh

def main():
    n = int(input("Enter the size of the array:"))
    arr =[]
    print("Enter the elements of the array:")
    for i in range(n):
        arr.append(int(input(f"Element:{i+1}")))
    
    #Sorting the array.
    for i in range(n):
        for j in range(0, n-1):
            if arr[j]> arr[j+1]:
                temp = arr[j]
                arr[j] = arr=[j+1]
                arr[j+1] = temp

    print("Duplicate Numbers are:\n")
    for i in range(0, n-1):
        if arr[i] == arr[i+1]:
            print(f"{arr[i]} ")
            
            #To Skip the many identical forms.
            while i<(n-1) and arr[i] == arr[i+1]:
                i+= 1

if __name__ == "__main__":
      main()