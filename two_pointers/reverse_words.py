def reverse_words(words):

    # convert str to list
    str = list(words)

    # edge case : empty string
    start = 0
    end = 0
    if len(str) == 0:
        return
    
    # ignore trailing spaces
    while end < len(str) and str[end] == " ":
        end += 1
    start = end

    # reverse each word
    while end < len(str):

        # increment end till you reach a space
        while end < len(str) and str[end] != " ":
            end += 1
        

        # reverse the word between start & end
        reverse_word(str, start, end-1)


        # move start and end to the start of next word
        while end < len(str) and str[end] == " ":
            end += 1
        start = end

    
    # reverse the whole string
    
    reverse_word(str, 0, len(str)-1)

    return "".join(str)


def reverse_word(str, start, end):
     while start < end:
        str[start],str[end] = str[end],str[start]
        start += 1
        end -= 1
        

str = "This is a nice string"
print(reverse_words(str))

str1 = "   This    is a nice  string  "
print(reverse_words(str1))