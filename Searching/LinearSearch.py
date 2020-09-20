def lns(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return f"element found at position {i+1}"
    return f"element not found the the list"


arr = [ 2, 3, 4, 10, 40 ]
print(lns(arr,3))
print(lns(arr,11))