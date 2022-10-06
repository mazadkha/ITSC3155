# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(s):
    dict3 = {}
    maxvalue = 0
    maxkey = "0"
    for i in s:
        if int(i) % 3 == 0 and int(i) > 2:
            # Adding key and values to dict3
            if i in dict3:
                dict3[i] += 1
            else:
                dict3[i] = 1
    for key, value in dict3.items():
        if value > maxvalue:
            maxvalue = value
            maxkey = key
    return int(maxkey)

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
    dictList = {}
    listKey = []
    i, j = 0, 1
    while i < len(s) and j < len(s):
        dictList[s[i]] = 1
        while j < len(s):
            if s[i] != s[j]:
                i = j
                j = i + 1
                break
            dictList[s[i]] += 1
            j += 1
    x = max(dictList.values())
    for key, value in dictList.items():
        if value == x:
            listKey.append(key)
    return listKey


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    s = s.replace(" ", "")
    srev = ''
    for i in range(len(s) - 1, -1, -1):
        srev = srev + s[i]
    return srev.lower() == s.lower()
