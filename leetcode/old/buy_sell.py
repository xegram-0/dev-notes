
def bestBuySell(stockList:list) -> str:
    buy:int = 0
    sell:int = 1
    currentProfit:int = 0
    maxProfit:int = 0
    while sell < len(stockList):
        if stockList[buy] < stockList[sell]:
            currentProfit = stockList[sell] - stockList[buy]
            maxProfit = max(maxProfit, currentProfit)
        else:
            buy = sell
        sell += 1
        


    return f"Max profit is {maxProfit}."
def main():
    stockList:list = [7,1,5,3,6,4,6,7,10]
    print(bestBuySell(stockList))
if __name__ == "__main__":
    main()