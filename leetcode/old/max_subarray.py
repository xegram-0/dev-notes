
def max_subArray(theList:list) -> int:
    maxSum:int = theList[0]
    currentMax = 0
    for number in theList:
        if currentMax < 0:
            currentMax = 0
        currentMax += number
        #print(currentMax)
        maxSum = max(currentMax, maxSum)

    return maxSum

def main():
    theList:list = [-2,-3,-4,-5,-6,-1,-3,-5]
    print(max_subArray(theList))

if __name__ == "__main__":
    main()