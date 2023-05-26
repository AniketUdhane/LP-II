def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the smallest element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the smallest element with the first element in the unsorted part of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Get user input for the array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Call the selection_sort function to sort the array using the greedy search algorithm
sorted_arr = selection_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
