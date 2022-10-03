


def longestWord(string):
    longest = ""
    a = string.split(' ') 
    for i in a:
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
    a = string.split(' ')
    reversedList = list[::-1]
    if len(a)>1:
        if reversedList == a:
            print("This string is a palindrome")
        else:
            print("This is not a palindrome")
    
    else:
        splittedList = list(string)
        reversedString = list(string)[::-1]
        
        if splittedList == reversedString:
            print(f"{string} is a Palindrome")
        else:
            print(f"{string} is not a palindrome")
        
    
def occurence(string):
    count = 0
    word = ""
    a = string.split(' ')
    for i in a:
        for k in a:
            if i == k:
                count += 1
                word = i
        print(f"Occurence of {word} is {count}")
        count = 0
    
    






string = str(input("Enter the string : "))


print(f"The longest word in string is {longestWord(string)}")


k = str(input("Enter the character whose occurence is to be shown : "))


print(f"The occurence of letter '{k}' is {freq(k,string)}")



print(isPalindrome(string))


print(occurence(string))