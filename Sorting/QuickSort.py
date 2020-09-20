def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def qks(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        qks(arr,low,pi-1)
        qks(arr,pi+1,high)
    return arr



arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
print(qks(arr,0,n-1))