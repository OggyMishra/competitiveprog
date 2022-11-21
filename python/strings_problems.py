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



if __name__ == '__main__':
    # region Longest substring without repeating characters
    # s = 'acbdbacd'
    # print('length of longest substring without repeating {}'.format(lengthOfLongestSubstring_approach_1(s)))
    # print('length of longest substring without repeating {}'.format(length_of_longest_substring_approach_2(s)))
    # endregion
