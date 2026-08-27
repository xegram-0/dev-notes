def recursive_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        result:int = recursive_fib(n-1) + recursive_fib(n-2)
    return result
    
def memorize_fib(n):
    memo:list = [None] * (n+1)
    return memorize_fibNext(n, memo)
def memorize_fibNext(n:int, memo:list):
    if memo[n] != None:
        return memo[n]
    elif n == 1 or n == 2:
        return 1
    else:
        result:int = memorize_fibNext(n-1, memo) + memorize_fibNext(n-1, memo)
    memo[n] = result
    return result

def bottomUp_fib(n):
    # faster exit
    if n == 1 or n == 2:
        return 1
    bottomUp:list = [None] * (n+1)
    bottomUp[1] = 1
    bottomUp[2] = 1
    for i in range(3, n+1):
        bottomUp[i] = bottomUp[i-1] + bottomUp[i-2] 
    return bottomUp[n]
def main():
    n:int = int(input("Enter n: "))
    print(recursive_fib(n))
    print(memorize_fib(n)) # this one has oddly index display
    print(bottomUp_fib(n))

if __name__ == "__main__":
    main()