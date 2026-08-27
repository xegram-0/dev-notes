def checkValid(theString:str):
    stack:list = []
    parentheseHashMap:dict = {')':'(',']':'[','}':'['}
    # start with closing parenthese and pop at the most behind in the list
    for char in theString:
        if char in parentheseHashMap:
            if stack and stack[-1] == parentheseHashMap[char]: # the check of matching
                stack.pop()
            else:
                return False
        else:
            stack.append(char) # if the stuff is the opening parenthese
    return True if not stack else False # stack has to be empty
def main():
    s1:str = "()"
    s2:str = "()[]"
    s3:str = "()[]{}" # what???
    s4:str = "((((((())))))"
    print(checkValid(s4))
if __name__ == "__main__":
    main()