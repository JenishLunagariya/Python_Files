def reversestr(string): # reverse a string
    e = len(string)-1
    ans = ""
    while e>=0:
        ans+=string[e]
        e-=1
    return ans
# string = "BoAt"
# print(reversestr(string))

def palindrome(string): # check for palindrome
    s = 0
    e = len(string)-1
    while s<=e:
        if string[s] != string[e]:
            return False
        s+=1
        e-=1
    return True
# string = "abdba"
# print(palindrome(string))

def reversewordsofstr(string):
    i=0
    n = len(string)
    ans = ""
    while i<n:
        while i<n and string[i] == " ":
            i+=1
        j = i+1
        while j<n and string[j] != " ":
            j+=1
        word = string[i:j]
        if ans == "":
            ans = word
        else:
            ans = word + " " + ans
        i = j+1
    return ans
# string = "The sky is blue"
# print(reversewordsofstr(string))

def getmaxoccuringchar(string):
    l = [0]*26
    for i in string:
        ch = ord(i)
        if ch >= ord('a') and ch <= ord('z'):
            num = ch - ord('a')
        elif ch >= ord('A') and ch <= ord('Z'):
            num = ch - ord('A')
        l[num]+=1
    maxx = 0
    index = 0
    for i in range(len(l)):
        if l[i]>=maxx:
            index = i
            maxx = l[i]
    return chr(index+ord('a'))
# string = "testsample"
# print(getmaxoccuringchar(string))

def switchspaceinatr(string):
    ans = ""
    for i in string:
        if i==" ":
            ans+="@40"
        else:
            ans+=i
    return ans
# string = "My name is jenish"
# print(switchspaceinatr(string))

def removeoccurences(string, part):
    while len(string) != 0 and string.find(part) != -1:
        string = string[:string.find(part)]+string[string.find(part)+len(part):]
    return string
# string = "daabcbaabcbc"
# part = "abc"
# print(removeoccurences(string,part))

def checkEqual(count1,count2):
    for i in range(len(count1)): # c1 and c2 have same len
        if count1[i] != count2[i]:
            return 0
    return 1

def checkinclusionofstr(string1,string2): # check s1's permutations are in s2
    count1 = [0]*26
    for i in range(len(string1)):
        num = ord(string1[i]) - ord('a')
        count1[num]+=1
    # traverse s2 str in window of size s1 length and compare
    # first window
    windowsize = len(string1)
    i = 0
    count2 = [0]*26
    while i<windowsize and i<len(string2):
        num = ord(string2[i])-ord('a')
        count2[num]+=1
        i+=1
    if checkEqual(count1,count2):
        return True
    
    # further windows
    while i < len(string2):
        newChar = string2[i]
        num = ord(newChar) - ord('a')
        count2[num]+=1

        oldChar = string2[i-windowsize]
        num = ord(oldChar) - ord('a')
        count2[num]-=1

        i+=1
        if checkEqual(count1,count2):
            return True
    return False
# s1 = "ab"
# s2 = "eidbaoo"
# s2 = "eibdaoo"
# print(checkinclusionofstr(s1,s2))

def removeduplicateadjacentfromstr(string): # remove duplicate adjacents
    i=0
    while i<len(string)-1:
        if string[i] == string[i+1]:
            string = string[:i]+string[i+2:]
            if i > 0:
                i-=1
        else:
            i+=1
    return string
# string = "azxxzy" # azxxzy->azzy -> ay
# print(removeduplicateadjacentfromstr(string))

def compress(strarr): # "aabbccc" -> len("a2b2c3") input: in form of list
    i=0
    ansIndex = 0
    n = len(strarr)
    while i<n:
        j = i+1
        while j<n and strarr[i]==strarr[j]:
            j+=1
        strarr[ansIndex] = strarr[i]
        ansIndex+=1
        count = j-i
        if count>1:
            cnt = str(count)
            strarr[ansIndex] = cnt
            ansIndex+=1
        i=j
    return ansIndex
strarr = ["a","b","b","c","c","c","c","s"]
print(compress(strarr))

