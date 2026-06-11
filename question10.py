def find_duplicates(arr):

    checked = []

    print("Duplicate elements are:")

    for i in arr:
        if arr.count(i) > 1 and i not in checked:
            print(i)
            checked.append(i)

arr = [10, 20, 30, 20, 40, 10, 50, 30]

find_duplicates(arr)
