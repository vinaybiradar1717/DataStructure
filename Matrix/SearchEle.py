def search(m,x):
    n = len(m)
    #   N square++++++++++++++++++++
    # for i in range(n):
    #     for j in range(n):
    #         if m[i][j] == x:
    #             return (i,j)
    # return -1

    # N +++++++++++++++++++++++ (for sorted rows )
    i = 0
    j = n-1
    while i < n and j >= 0:
        if m[i][j] == x:
            return (i,j)
        if m[i][j] > x:
            j -= 1
        else:
            i += 1

l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(search(l, 10))