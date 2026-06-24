def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr=[23,11,12,9,5,7]
print(insertion_sort(arr))
# case 1
# for i in range (1,6): len(arr) = 6
# key = arr[1] = 11
# j = i -1 = 0
# while 0>=0 and arr[j] = arr[0] = 23 > key = 11; #true
# arr[j+1] = arr[1] = arr[j] = arr[0] when the above statment is true
# [23,23,12,9,5,7]
# [23,23,23,9,5,7]
