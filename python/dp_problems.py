# region Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#
# Example 2:
# Input: n = 1
# Output: ["()"]
from typing import List

def generate_parenthesis_using_recursive_approach(n:int) -> List[str]:
    res = []
    def dfs(left, right, s, count):
        # think about base case
        # base case is that the string length cannot exceed 2*n, since there are two parenthesis only.
        if len(res) == 2 * count:
            res.append(s)
            return

        # think about conditions
        # if left index is less then n then we should keep adding (
        if left < count:
            dfs(left + 1, right, s, count)
        # if right index is not less then left then keep adding )
        if right < left:
            dfs(left, right + 1, s, count)

    dfs(0, 0, '', n)
    return res










def generate_parenthesis_using_iterative_approach(n: int) -> List[str]:
    # complexity: Time = 4^n, space = not sure.
    res = []
    # initialize it with ( as all valid parenthesis needs to be started with (
    stack = [('(', n - 1, n)]
    while stack:
        item = stack.pop()
        s = item[0]
        o = item[1]
        c = item[2]

        if o == 0 and c == 0:
            res.append(s)
        else:
            if o != 0:
                stack.append((s+'(', o-1, c))
            if o < c:
                stack.append((s+')', o, c-1))

    return res
# endregion


if __name__ == '__main__':
    # region Generate Parenthesis
    n = 3
    print(generate_parenthesis_using_recursive_approach(n))
    # endregion
