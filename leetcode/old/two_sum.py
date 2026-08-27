def twoSum(theList:list, theValue:int):
    hashMap = {}
    #print(theList, theValue)
    for i, n in enumerate(theList):
        #print(i,n)
        diff = theValue - n
        if diff in hashMap:
            #print(hashMap, diff, n)
            return [diff,n]
        hashMap[n] = i # the element in the list : index
    return "There is no sum met the value"

def main():
    givenList:list = [3,4,6,7,11] # should be 6 and 7
    targetValue:int = 7
    print(twoSum(givenList, targetValue))

if __name__ == "__main__":
    main()