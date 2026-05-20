# Program to find the Majority Number in a single dimension array. 
# TriTea@blackpharaoh

def main():
    n= int(input("Enter the size of array:"))
    arr = []

    print("Enter the elements of array:")
    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element:")))

    #Selection sorting applied.
    for i in range(n-1):
        md = i;
        for j in range(i+1,n):
            if arr[j]<arr[md]:
              md = j
        
        temp = arr[md]
        arr[md] = arr[i]
        arr[i] = temp
    
    cd = arr[n//2]
    f = -1
    l = -1

    #Binary search is applied.
    low,high = 0, n-1
    while low <= high:
        mid = low + high-low//2
        if arr[mid] == cd:
            f = mid
            high = mid-1
        elif arr[mid]>cd:
            high = mid-1
        else :
            low = mid+1
    
    low,high = 0, n-1
    while low <= high:
        mid = low + high-low//2
        if arr[mid] == cd:
            l = mid
            low = mid+1
        elif arr[mid]>cd:
            high = mid-1
        else :
            low = mid+1

    ct = l - f+1
    if ct > n//2:
        print(f"\nThe majority element is: {cd}(appears {ct} times)")
    else:
        print("No Majority element exist!")
    
if __name__ == "__main__":
      main()