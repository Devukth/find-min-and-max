# find_min() and find_max()
def find_min(arr):
    minvar = 100000

    for i in range(len(arr)):
        if (minvar > arr[i]):
            minvar = arr[i]

    return minvar

def find_max(arr):
    maxvar = -100000

    for i in range(len(arr)):
        if (maxvar < arr[i]):
            maxvar = arr[i]

    return maxvar


arr1 = [1,5,2,7,3,9,10]
arr2 = [-999,2,4,7,23,6,2]
print(find_max(arr1))
print(find_min(arr2))