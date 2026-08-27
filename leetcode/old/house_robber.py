
def houseRob(givenHouse:list) -> str:
    robHouse1:int = 0
    robHouse2:int = 0
    houseRobbed:list = []
    for num in givenHouse:
        currentSum:int = max(robHouse1 + num, robHouse2)
        #houseRobbed.append(max(robHouse1 + num, robHouse2))
        robHouse1 = robHouse2
        robHouse2 = currentSum
    
    #print(houseRobbed)
    return f"The max profit is {robHouse2}."

def houseRob2(givenHouse:list) -> str:
    robHouse1:int = givenHouse[0]
    robHouse2:int = max(givenHouse[0],givenHouse[1])
    for i in range(len(givenHouse)):
        robHouse2 = max(robHouse1[i-2] + givenHouse[i], robHouse2[i-1])


    return f"{robHouse2}"
def main():
    givenHouse:list = [2,7,3,1,4,2,1,8]
    #print(houseRob(givenHouse))
    print(houseRob2(givenHouse))

if __name__ == "__main__":
    main()