# region To find the sum of n natural numbers
import math


# o(n) complexity
def sum_1(n):
    sum = 0
    for i in range(1, n):
        sum += i
    return sum


# o(1) complexity
def sum_2(n):
    return n * (n-1) // 2

# endregion


# region to find the gcd of two numbers
# using euclid algo the complexit of finding the gcd is o(logn)
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
# endregion


# region to find the lcm of two numbers
# formula for lcm
# product (a*b) = hcf * lcm
def lcm(a, b):
    return a * b // gcd(a, b)
# endregion

# region all divisor of a number
# n = 24
# [1,2,3,4,6,8,12,24]
# first & last number product is same as number
def get_divisor1(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

def get_divisor2(n):
    div = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
    return list(div)

# endregion

# region Compare Primality Test
# Prime No are those numbers which is divisible b 1 & itself.
#
def approach1(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


def approach2(n):
    # here idea is to find best way to check for primality of a number:
    # first step is to check if a number is 0 or 1 offcourse it's not a prime number
    if n == 0 or n == 1:
        return False
    # second step is to check if a number is 2 or 3 then it's prime number
    if n == 2 or n == 3:
        return True
    # third check if the number is divisible by 2 or 3 then it's not a prime number
    if n % 2 == 0 or n % 3 == 0:
        return False
    # using the same logic go on & use the generic logic and start from 5
    # here logic is similar to above if a number is divisible by 5 & 7 then it's not prime number.
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# endregion

# region
# To find the prime number upto n
# for each number 1 to n: o(n) and then check if i is prime or not o(sqrt(n)). T.C = N*root(N)
# better approach use Seive Theorem
def gen_primes(n):
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
    for i in range(2, len(primes)):
        if primes[i]:
            print(i, end=" ")
# endregion

if __name__ == '__main__':
    # region to print all the prime number upto n O(n*log(log(n))
    # -- gen_primes(150)

    # region sumofn numbers
    # -- print('Sum using O(1) complexity = {}'.format(sum_2(103223423423)))
    # -- print('Sum using O(n) complexity = {}'.format(sum_1(103223423423)))
    # endregion

    # region gcd of two numbers using euclid algo
    # -- print('gcd of two numbers = {}'.format(gcd(10, 50)))
    # endregion

    # region lcm of two numbers
    # -- print('lcm of two numbers = {}'.format(lcm(10, 50)))
    # endregion

    # region all divisor of a number
    # -- print('all divisor of {} in o(n) = {}'.format(24, get_divisor1(24)))
    # -- print('all divisor of {} in o(sqrt(n)) = {}'.format(24, get_divisor2(24)))
    # endregion

    # region prime number
    # -- print("checking primiality of a number using o(n) = {}".format(approach1(575887587587578)))
    # -- print("checking primiality of a number using o(sqrt(n)) = {}".format(approach2(911)))
    # endregion

