# region Longest substring without repeating characters

# To, find out a sliding window problem :-
# > First thing is, we have given something like an "Array" | OR | "String"
# > Second thing is, they are talking about either "subsequence" | OR | "substring"
# > And third most thing is, either we have given a "window size i.e. k" | OR | we have to "manually find out window size"
# Approach 2
# indext    0    1    2    3   4   5   6   7
# string    a    c    b    d   b   a   c   d
#           ^                  ^
#           |                  |
# 		left               right
# 		seen = {a : 0, c : 1, b : 2, d: 3}
# 		# case 1: seen[b] = 2, current window  is s[0:4] ,
# 		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
# 		seen = {a : 0, c : 1, b : 4, d: 3}
# indext    0    1    2    3   4   5   6   7
# string    a    c    b    d   b   a   c   d
# 						 ^   ^
# 					     |   |
# 				      left  right
# indext    0    1    2    3   4   5   6   7
# string    a    c    b    d   b   a   c   d
# 					     ^       ^
# 					     |       |
# 				       left    right
# 		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3
# 		# we can keep moving right pointer.


def lengthOfLongestSubstring_approach_1(s: str) -> int:
    i = 0
    j = 0
    longest = -1
    sub_char_map = dict()

    if len(s) == 0:
        return 0

    while j < len(s):
        if s[j] in sub_char_map:
            sub_char_map[s[j]] += 1
        else:
            sub_char_map[s[j]] = 1

        if len(sub_char_map) == (j - i + 1):
            longest = max(longest, j - i + 1)
            j += 1
        elif len(sub_char_map) < (j - i + 1):
            # print(j)
            # print(i)
            while len(sub_char_map) < j - i + 1:
                sub_char_map[s[i]] -= 1
                # print(sub_char_map)

                if sub_char_map[s[i]] == 0:
                    sub_char_map.pop(s[i])

                i += 1

            j += 1
    return longest


def length_of_longest_substring_approach_2(s: str) -> int:
    l = 0
    seen = dict()
    longest = 0
    for r in range(len(s)):
        if s[r] in seen:
            if seen[s[r]] >= l:
                l = seen[s[r]] + 1
        seen[s[r]] = r
        longest = max(longest, r - l + 1)

    return longest
# endregion

# region Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"

def longest_palindrome(s: str) -> str:
    return 4%6

# endregion

# region ZigZag String Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:

def convert_to_zig_zag(s:str, num_rows:int)->str:
    template = list(range(num_rows)) + (list(range(num_rows-2, 0, -1)))
    buckets = [''] * len(template)
    for i, char in enumerate(s):
        buckets[template[i % len(template)]] += char

    return''.join(buckets)

# endregion

# region Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
#
# Input: s = "()"
# Output: true

# Example 2:
#
# Input: s = "()[]{}"
# Output: true


# Example 3:
#
# Input: s = "(]"
# Output: false

def is_valid_parenthesis(s:str)-> bool:
    brackets = []
    for i, char in enumerate(s):
        if brackets:
            if brackets[-1] == '{' and char == '}':
                brackets.pop()
            elif brackets[-1] == '(' and char == ')':
                brackets.pop()
            elif brackets[-1] == '[' and char == ']':
                brackets.pop()
            else:
                brackets.append(char)
        else:
            brackets.append(char)

    if len(brackets) > 0:
        return False
    else:
        return True


# endregion

if __name__ == '__main__':
    # region Longest substring without repeating characters
    # s = 'acbdbacd'
    # print('length of longest substring without repeating {}'.format(lengthOfLongestSubstring_approach_1(s)))
    # print('length of longest substring without repeating {}'.format(length_of_longest_substring_approach_2(s)))
    # endregion

    # region Longest Palindromic Substring
    #print('longest palindromic string {}'.format(longest_palindrome('babad')))
    # endregion

    # region ZigZag String conversion
    # s = 'PAYPALISHIRING'
    # print('ZigZag pattern will be {}'.format(convert_to_zig_zag(s, 3)))
    # endregion

    # region IsValidParentheses
    s = '([{[}])'
    print('Is valid parentheses for given string = {}'.format(is_valid_parenthesis(s)))
    # endregion

