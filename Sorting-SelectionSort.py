# Sorting - Selection Sort
# Iteratively find the minimum value in one sub-array and keep inserting it to the sorted sub-array


def selection_sort(a):
    for i in range(len(a)):
        for j in range((i + 1), len(a)):
            if a[i] > a[j]:
                key = a[i]
                a[i] = a[i + 1]
                a[i + 1] = key

    return a


if __name__ == '__main__':

    # Prompt the user to enter space separated integer array values
    print('Enter space separated array elements to be sorted:')

    # Read the array elements from the input
    arr = list(input().split())

    # Convert the string input to integer values
    arr = [int(i) for i in arr]

    # Call the function for insertion sort
    arr = insertion_sort(arr)

    # Output:
    print('Sorted Array:')
    for i in arr:
        print(i, end=' ')
