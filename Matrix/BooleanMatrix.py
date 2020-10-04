
#       wrong +++++++++++++++++++++++++++++

def boolmat(m):
    n = len(m)
    k = m
    print("Before:")
    print(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] == 0:
                k[i][j] = 1
            elif m[i][j] == 1:
                k[i][j] == 0
            else:
                continue
                #k[i][j] = 0
    print("After:")
    return k

l = [[1, 0, 0, 1],[0, 0, 1, 0],[0, 0, 0, 0],[0, 0, 1, 0]]
print(boolmat(l))