# Attempt
class Solution:
    def decodeString(self, s: str) -> str:
        textString = ""
        num = 0
        numStack = []
        stringStack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                numStack.append(num)
                stringStack.append(textString)
                num = 0
                textString = ''
            elif c == ']':
                previousNum = numStack.pop()
                previousStr = stringStack.pop()
                textString = previousStr + textString * previousNum
            else:
                textString += c
        return textString
                
