# Program to find and solve the 3-Sum problem in a 1D Array.
# TriTea@blackpharaoh

def main():
    n = int(input("Enter the size of array:"))

    arr =[]
    print("Enter the elements of array:")
    for i in range(n):
        arr.append(int(input(f"Element {i+1}")))
    
    #Sorting with Selection
    for i in range(n-1):
        md=i
        for j in range(i+1, n):
            if arr[j]< arr[md]:
                md =j
        temp = arr[md]
        arr[md]= arr[i]
        arr[i]= temp
    
    print("\nTriplet that summ upto 0 are:\n")
    fd = False

    for i in range(n-2):      # We are using two pointer approach to solve.
        if i>0 and arr[i]==arr[i-1]:
            continue

        left = i+1
        right = n-1

        while left<right:
            total = arr[i]+arr[left]+arr[right]
            if total == 0:
                print(f"[{arr[i]}, {arr[left]}, {arr[right]}]")
                fd = True
                
                while left<right and arr[left] == arr[left+1]:
                    left += 1
                while left< right and arr[right] == arr[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total <0:
                left += 1
            else:
                right-=1
    
    if not fd:
        print("No triplet found!")

if __name__ == "__main__":
    main()