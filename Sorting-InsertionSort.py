# Sorting - Insertion Sort


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            key = a[j]
            a[j] = a[j - 1]
            a[j - 1] = key
            j -= 1
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
