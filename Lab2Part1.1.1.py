# Vi har ett basfall med längden 3 och plockar alltid 
# bort det sista elementet från arrayen. Påvägen upp från rekursionen 
# så jämför vi det med basfallet, om det hör hemma till det tre minsta.

#T(n) = O(N)
countComp = 0

# Sorts the base case
def get3min(a):
    global countComp
    countComp += 1
    if(len(a) == 3):
        countComp += 1
        if(a[0] > a[1]):
            temp = a[0]
            a[0] = a[1]
            a[1] = temp
        countComp += 1
        if(a[1] > a[2]):
            temp = a[1]
            a[1] = a[2]
            a[2] = temp
        countComp += 1
        if(a[0] > a[1]):
            countComp += 1
            temp = a[0]
            a[0] = a[1]
            a[1] = temp
        return (a)
    
    # Pops last element from array a, and on the way on the recursion
    # sorts it into the list of minimum three elements to be returned, if neccessary
    eliminatedElement = a.pop(-1)
    min3 = get3min(a)
    # If EE is smaller than the biggest one in the sorted basecase
    countComp += 1
    if(eliminatedElement < min3[2]):
        # but bigger than the second, we have to replace it as the last in list of three
        countComp += 1
        if(eliminatedElement > min3[1]):
            min3[2] = eliminatedElement
        # if EE is bigger than first but smaller than second, we need to insert it inbetween
        # with the help of temp.var.
        countComp += 2
        if(eliminatedElement > min3[0] and eliminatedElement < min3[1]):
            temp = min3[1]
            min3[1] = eliminatedElement
            min3[2] = temp
        # If EE is the smallest one, this is how we insert it first while pushing 2nd and 
        # 3rd one forward w. two temp.var
        countComp += 1
        if(eliminatedElement < min3[0]):
            temp1 = min3[0]
            temp2 = min3[1]
            min3[0] = eliminatedElement
            min3[1] = temp1
            min3[2] = temp2
    return min3

a = []
print("The smallest elements are: ",get3min(a))
print("The Number of comparisons are: ",countComp)