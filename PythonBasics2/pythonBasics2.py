# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) return the multiple of three that
# occurs the most in a string. For example, 0939639 would return 9 since
# it appeared 3 times while the other multiple of three appeared less than that.
# You only need to worry about single digit multiples of 3 (3, 6, 9).

def count_threes(s):
    dict3 = {}
    maxvalue = 0
    maxkey = "0"
    # Adding key and values to dict3
    for i in s:
        if int(i) % 3 == 0 and int(i) > 2:
            if i in dict3:
                dict3[i] += 1
            else:
                dict3[i] = 1
    # Iterating through the values for maximum value and setting the max key
    for key, value in dict3.items():
        if value > maxvalue:
            maxvalue = value
            maxkey = key
    return int(maxkey)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that return a list
# containing all characters with the longest consecutive repeat. For example,
# the longest_consecutive_repeating_char('aabbccd') would return ['a', 'b', 'c']
# (order doesn't matter).
def longest_consecutive_repeating_char(s):
    dictList = {}
    listKey = []
    i, j = 0, 1
    # Creating a dictionary with the keys as consecutive character and values as the number of repetition
    while i < len(s) and j < len(s):
        dictList[s[i]] = 1
        while j < len(s):
            if s[i] != s[j]:
                i = j
                j = i + 1
                break
            dictList[s[i]] += 1
            j += 1
    # Setting x as the maximum value found in the dictionary
    x = max(dictList.values())
    # Finding the keys with the maximum value
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
