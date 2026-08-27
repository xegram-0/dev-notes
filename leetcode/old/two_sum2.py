def twoSum1(theList:list, target:int) -> str:
    hashMap = {}
    for i, num in enumerate(theList):
        diff = target - num
        hashMap[num] = i
        if diff in hashMap:
            print(hashMap)    
            return f"The sum of {diff} and {num} is {target}. Therefore index1 = {hashMap[diff]}, index2 = {hashMap[num]}."
    return f"Cannot meet the target"

# using sliding window
def twoSum2(theList:list, target:int) -> str:
    left:int = 0
    right:int = len(theList) - 1
    currentSum:int = 0
    while left < right:
        currentSum = theList[left] + theList[right]
        if currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
        else:
            return f"The sum of {theList[left]} and {theList[right]} is {target}. Therefore index1 = {left} and index2 = {right}"
    
def main():
    givenArray:list = [2,3,4,14,19,63,87,100]
    for i, num in enumerate(givenArray):
        print(f"{i}: {num}")
    target:int = 65
    #print(twoSum1(givenArray, target))
    print(twoSum2(givenArray, target))
if __name__ == "__main__":
    main()