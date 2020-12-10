def getBestSubArr(a):
    globMax = maxSubProd(a)
    #return globMax[1], globMax[3]
    return globMax[3]

def maxSubProd(a):
    n = len(a)
    if n == 1:
        return (a, a, a[0], a[0])

    lastElement = a.pop()

    localMax = maxSubProd(a)
    localProd = localMax[2]
    globalProd = localMax[3]

    localMaxArr = list(localMax[0])
    globalMaxArr = list(localMax[1])

    if localProd*lastElement >= lastElement:
        localMaxArr.append(lastElement)
        newLocalProd = localProd * lastElement
        
    elif localProd*lastElement <= lastElement :
        localMaxArr = []
        localMaxArr.append(lastElement)
        newLocalProd = lastElement

    if(newLocalProd >= globalProd):
        globalMaxArr = []
        globalMaxArr += localMaxArr
        globalProd = newLocalProd
    return (localMaxArr, globalMaxArr, newLocalProd, globalProd)

a = []
print(getBestSubArr(a))