# T(n) = Theta(nlogn)

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

    minimum = min(leftQuota[0])
    maximum = max(rightQuota[0])

    maxQuota = max(leftQuota[1], rightQuota[1], maximum/minimum)

    return ([minimum,maximum], maxQuota)

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

A = [14,1,2,4,6,9,10,12]
print("Högsa kvot kommer att vara:",bruteForce(A))
print("Uträknad kvot blev:",maxQuotient(A))

