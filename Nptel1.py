'''
def intreverse(n):
    if n > 0:
        r = n % 10
        q = n // 10
        print(r, end='')
        return intreverse(q)


intreverse(783)
'''

'''
Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

  >>> intreverse(783)
  387
  >>> intreverse(242789)
  987242
  >>> intreverse(3)
  3
'''


def intreverse(n):
    x = str(n)
    if len(x) == 1:
        return (n)

    else:
        endmsg = ""
        for i in range(0, len(x)):
            endmsg = x[i] + endmsg
        return (endmsg)


intreverse(783)

'''
Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.

 
  >>> matched("zb%78")
  True
  >>> matched("(7)(a")
  False
  >>> matched("a)*(?")
  False
  >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
  True
'''


def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


matched("(7)(a")

'''
Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

  >>> sumprimes([3,3,1,13])
  19
  >>> sumprimes([2,4,6,9,11])
  13
  >>> sumprimes([-3,1,6])
  0
'''


def sumprimes(l):
    sum = 0
    for i in l:
        if i > 1:
            prime = True
            for j in range(2, i):
                if (i % j == 0):
                    prime = False
            if prime:
                sum = sum + i

    return (sum)


sumprimes([3, 3, 1, 13])

