# Check whether a string as a palindrome or not
def is_palindrome(str):
    left = 0
    right = len(str) - 1
    while left <= right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True



if __name__ == "__main__":

    str1 = "HelloWorld"
    print(str1, ":", is_palindrome(str1))



    str2 = "abba"
    print(str2, ":", is_palindrome(str2))