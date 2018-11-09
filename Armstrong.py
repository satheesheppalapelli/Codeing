# Function to check whether the given number is
# Armstrong number or not

"""
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Input : 1253
Output : No
1253 is not a Armstrong Number
1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723

Input : 1634
Output : Yes
1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634

"""

def isArmstrong(num):
    order = len(str(num))
    # initialize sum
    sum = 0
    # find the sum of the cube of each digit
    temp = num
    while temp > 0 and temp != 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    # display the result if number is true...
    if num == sum:
        return str(num) + ' is a Armstrong Number'
    else:
        return str(num) + ' Not a Armstrong Number'


a = isArmstrong(153)
b = isArmstrong(120)
c = isArmstrong(1253)
d = isArmstrong(1634)
print(a)
print(b)
print(c)
print(d)
