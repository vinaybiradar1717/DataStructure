def bns(arr,l,r,x):
    if r>=l:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid+1
        if arr[mid] > x:
            return bns(arr,0,mid-1,x)
        else:
            return bns(arr,mid+1,r,x)
    else:
        return f"Element {x} is not in the list"






arr = [ 2, 3, 4, 10, 40 ]
n = len(arr)
a = bns(arr,0,n-1,10)
print(f"Element found at position {a}")
a = bns(arr,0,n-1,33)
print(f"Element found at position {a}")