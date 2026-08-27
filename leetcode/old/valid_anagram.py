from collections import Counter

def isAnagram(str1:str, str2:str):

    print(f"Is {str1} an anagram of {str2}?")
    #return sorted(str1) == sorted(str2)
    #return Counter(str1) == Counter(str2)
    if len(str1) != len(str2):
        return False
    
    hashStr1, hashStr2 = {}, {}
    
    for i in range(len(str1)):
        hashStr1[str1[i]] = 1 + hashStr1.get(str1[i], 0) # if the var is not existed yet, make it default value = 0
        hashStr2[str2[i]] = 1 + hashStr2.get(str2[i], 0)

    for char in hashStr1:
        if hashStr1[char] != hashStr2.get(char, 0): # in case there is no character shared between 2 strings
            return False
    return True

def main():
    # case sensitive
    str1:str = "Mama"
    str2:str = "Fefe"
    print(isAnagram(str1,str2))
if __name__ == "__main__":
    main()