# T(n) = Theta(n)

def maxQuotient(A):
    # Base case
    if len(A) == 2:
        return (A, (A[1]/A[0]))

    # Splits array A in left and right parts
    leftA = A[:len(A)//2]
    rightA = A[len(A)//2:]

    # Recursion call
    leftQuota = maxQuotient(leftA)
    rightQuota = maxQuotient(rightA)

    # List for keeping track of min and max element in A
    minMax = []

    # Concatenate list and sort it
    sortedList = (leftQuota[0]+rightQuota[0])
    sortedList = sorted(sortedList)

    # Appends min and max element to list minMax
    minMax.append(sortedList[0])
    minMax.append(sortedList[3])
    # Current max quota
    maxQuota = max(leftQuota[1], rightQuota[1])

    # Compares other possibilites of quotas to 
    for denominator in leftQuota[0]:
        for numerator in rightQuota[0]:
            if numerator/denominator > maxQuota:
                maxQuota = numerator/denominator

    return (minMax, maxQuota)

def getMaxQuotient(A):
    quota = maxQuotient(A)
    return quota[1]

# Just a bruteForce for calculating the biggest quota.
# Used only for comparison with our own algorithm.
def bruteForce(A):
    maxKvot = (A[1]/A[0])
    i = 0
    j = 0
    while j < len(A):
        while i < j:
            täljare = A[j]
            nämnare = A[i]
            if täljare/nämnare > maxKvot:
                maxKvot = täljare/nämnare
            i += 1
        i = 0
        j += 1
    return maxKvot

A = [2,8,20,1,3,5,6,4]
print("Högsa kvot kommer att vara:",bruteForce(A))
print("Uträknad kvot blev:",maxQuotient(A))

