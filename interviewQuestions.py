def isMegaPalindrome(myStr):
    if (len(myStr) % 2) != 0: 
        halfway_index = (int)(len(myStr)/2)
        i = 0
        while halfway_index - i >= 0:
            if myStr[halfway_index + i] != myStr[halfway_index - i]:
                return False
            i += 1
        return True
    
    else:
        halfway_index_R = (int)(len(myStr)/2)
        halfway_index_L = halfway_index_R - 1
        i = 0
        
        while halfway_index_L - i >= 0:
            if myStr[halfway_index_L - i] != myStr[halfway_index_R + i]:
                return False
            i += 1
        return True


def isNormalPalindrome(myStr):
    myStr = myStr.lower()
    return isMegaPalindrome(myStr)


def runPalindrome(myStr):
    print(f"Is '{myStr}' Normal Palindrome: {isNormalPalindrome(myStr)}")
    print(f"Is '{myStr}' Mega Palindrome: {isMegaPalindrome(myStr)}")


def reverseString(myStr):
    list_char = list(myStr)
    indexL = 0
    indexR = len(myStr) - 1

 
    while indexL < indexR:
        temp = list_char[indexL]
        list_char[indexL] = list_char[indexR]
        list_char[indexR] = temp

        indexL += 1
        indexR -= 1
    

    reversedStr = ''.join(list_char)
    return reversedStr


def runReverseString(myStr):
    print(f"Orginal word: {myStr} \nReversed Word: {reverseString(myStr)}")


def longestCommonPrefix(myList):
    if len(myList) == 0: return ""
    elif len(myList) == 1: return myList[0]

    else:
        min_length = min(len(str) for str in myList)
        for j in range(min_length + 1):
            for i in range(len(myList)):
                if (j > min_length - 1) or (myList[0][j] != myList[i][j]):
                    return myList[0][0:j]


def runLongestCommonPrefix(myList):
    print(f"In the list of words: '{myList}', the longest common prefix is '{longestCommonPrefix(myList)}'.")


def numeralToInteger(myStr):
    if len(myStr) == 0: return ""

    def getValue(r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1

    if len(myStr) == 1: return getValue(myStr)

    else:

        i = 1
        length = len(myStr) - 1
        total = getValue(myStr[length])
        while i <= length:
            if (getValue(myStr[length - i])) < (getValue(myStr[length])):
                total -= getValue(myStr[length - i])
                
            else:
                total += getValue(myStr[length - i])

            i += 1
        return total

def runRomanNumeral(myStr):
    print(f"The Roman numeral {myStr} is equivalent to the integer {numeralToInteger(myStr)}.")
    


def main():
    #runPalindrome("Natan")
    #runReverseString("Hello")
    #runLongestCommonPrefix(["flower", "flow"])
    runRomanNumeral("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXIVXLXIXCCCDLCLDXXXIXXIXLIXXIXV")


if __name__ == '__main__':
    main()