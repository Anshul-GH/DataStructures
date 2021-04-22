# Sorting - Bubble Sort
# Iteratively compare the consecutive values in pair


def bubble_sort(a):

    srt_flg = False
    while not srt_flg:
        srt_flg = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                srt_flg = False
                a[i], a[i + 1] = a[i + 1], a[i]
                '''
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                '''
            print(i, '->', a)

    return a


if __name__ == '__main__':

    # Prompt the user to enter space separated integer array values
    print('Enter space separated array elements to be sorted:')

    # Read the array elements from the input
    arr = list(input().split())

    # Convert the string input to integer values
    arr = [int(i) for i in arr]

    # Call the function for insertion sort
    arr = bubble_sort(arr)

    # Output:
    print('Sorted Array:')
    for i in arr:
        print(i, end=' ')
