# Python program for implementation of MergeSort 

# Time Complexity: O(n log n)
# Space Complexity: O(n)

def mergeSort(arr):
    if len(arr) > 1:
        
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array into two halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)
        
        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Merging the two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
