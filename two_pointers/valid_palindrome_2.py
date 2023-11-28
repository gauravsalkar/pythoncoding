def is_palindrome(str, i, j):
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

def valid_palindrome_2(str):
    i = 0
    j = len(str) - 1

    while i < j:
        if str[i] != str[j]:
            return is_palindrome(str, i+1, j) or is_palindrome(str, i, j-1)
        i += 1
        j -= 1
    return True

str1 = "RACEACAR"
print(str1, " : ", valid_palindrome_2(str1))


str2 = "madame"
print(str2, " : ", valid_palindrome_2(str2))

str3 = "dead"
print(str3, " : ", valid_palindrome_2(str3))

str4 = "eeccccbebaeeabebccceea"
print(str4, " : ", valid_palindrome_2(str4))