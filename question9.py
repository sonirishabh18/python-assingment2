def count_frequency(arr):

    for i in arr:
        count = arr.count(i)
        print(i, "->", count, "times")

arr = [1, 2, 2, 3, 1, 4, 2]

count_frequency(arr)
