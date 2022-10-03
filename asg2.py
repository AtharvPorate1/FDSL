from itertools import count


def longestWord(string):
    longest = ""
    list = string.split(' ') 
    for i in list:
        if len(i) > len(longest):
            longest = i
    return longest


def freq(k,string):
    count = 0
    for i in string:
        if k == i:
            count += 1
    
    return count

def isPalindrome(string):
    list = string.split(' ')
    reversedList = list[::-1]
    if len(list)>1:
        if reversedList == list:
            print("This string is a palindrome")
        else:
            print("This is not a palindrome")
    
    else:
        reversedString = string.reverse()
        if string == reversedString:
            print("This is a Palindrome")
        else:
            print("This is not a palndrome")
        
    
def occurence(string):
    count = 0
    word = ""
    list = string.split(' ')
    for i in list:
        for k in list:
            if i == k:
                count += 1
                word = i
        print(f"Occurence of {word} is {count}")
    
    






string = str(input("Enter the string : "))


print(f"The longest word in string is {longestWord(string)}")


k = str(input("Enter the character whose occurence is to be shown : "))


print(f"The occurence of letter '{k}' is {freq(k,string)}")



print(isPalindrome(string))


print(occurence(string))