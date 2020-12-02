#T(n) = O(n)

opCounter = 0
def get3Min(a):
    global opCounter
    opCounter = opCounter + 1
    # Base case, sort three elements and return the array
    if(len(a) == 3):
        a.sort()
        return (a)

    # Splits array a, into left- and right halves
    lefta = a[:len(a)//2]
    righta = a[len(a)//2:]
    
    # Recursion call on each half
    leftMin = get3Min(lefta)
    rightMin = get3Min(righta)

    # combines each of the halves into a combined list,
    # sorts it and return the three minimum elements
    combMinLst = leftMin + rightMin
    combMinLst.sort()

    return combMinLst[:3]


# a = []    
print("The smallest elements are:",get3Min(a))
print("The number of comparisons are:",opCounter)