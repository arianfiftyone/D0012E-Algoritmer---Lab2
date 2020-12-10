def maxSubProd(a):

    if len(a) == 1:

        return ([a[0]], [a[0]])

    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]

    leftP = maxSubProd(left)
    rightP = maxSubProd(right)
    
    # localmax och localmin för left är klart
    localMax = leftP[0]
    localMin = leftP[1]

    # uppdatera localmax och localmin för right
    i = 0
    while i < mid:
        # localmax[i] = max(a[i], a[i] * localmax[i - 1])
        localMax.append(max(rightP[0][i], a[i + mid]*localMax[i+mid-1], a[i + mid] *localMin[i+mid-1]))
        localMin.append(min(rightP[1][i], a[i + mid]*localMax[i+mid-1], a[i + mid] *localMin[i+mid-1]))
        i = i + 1

    return (localMax, localMin)


a = []
p = maxSubProd(a)
maxP = max(p[0])
minP = min(p[1])
print(maxP, ", ", minP)



    
    

