def ins(arr):
    n = len(arr)
    c = 0
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        c += 1

    return [arr,c]
arr = [1,2,5,3,7,8,6,4]
#arr = [64, 34, 25, 12, 22, 11, 90]
print(ins(arr))