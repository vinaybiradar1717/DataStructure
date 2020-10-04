def spiral(m):
    n = len(m)
    T = L = 0
    B = R = n-1
    dirt = 0
    sp = []
    while T<=B and L<=R:
        if dirt == 0:
            for i in range(L,R+1):
                sp.append(m[T][i])
            T += 1
        elif dirt == 1:
            for i in range(T,B+1):
                sp.append(m[i][R])
            R -= 1
        elif dirt == 2:
            i = R
            while i>=L:
                sp.append(m[B][i])
                i -= 1
            B -= 1
        elif dirt == 3:
            i = B
            while i>=T:
                sp.append(m[i][L])
                i -= 1
            L += 1
        dirt = (dirt+1)%4
    return sp
    
l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiral(l))