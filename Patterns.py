for i in range(0, 4):
    # *
    # *
    # *
    # *
    print('*')

print('**************************************')

for i in range(0, 4):
    # * * * *
    print('*', end=' ')

print('\n**************************************')

'''
    ****
    ****
    ****
    ****
'''

# row
for i in range(0, 4):
    # column
    for j in range(0, 4):
        print('*', end='')
    print("\r")
print('**************************************')

'''
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
'''
num = 1
for i in range(0, 4):
    for j in range(0, 4):
        print(num, end=' ')
        num += 1
    print("\r")

print('**************************************')

'''
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4
'''
num = 1
for i in range(0, 4):
    for j in range(0, 4):
        print(num, end=' ')
    num += 1
    print("\r")

print('**************************************')

'''
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4
'''

for i in range(0, 4):
    num = 1
    for j in range(0, 4):
        print(num, end=' ')
        num += 1
    print("\r")

print('**************************************')

'''
1 1 1 1 
1 1 1 1 
1 1 1 1 
1 1 1 1
'''
for i in range(0, 4):
    num = 1
    for j in range(0, 4):
        print(num, end=' ')
    # num += 1
    print("\r")

print('**************************************')


'''
1 2 3 4 
2 4 6 8 
3 6 9 12 
4 8 12 16 
'''
num = 1
for i in range(1, 5):
    for j in range(1, 5):
        print(j * i, end=' ')
    num += 1
    print('\r')

print('**************************************')

'''
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *
'''
for i in range(0, 6):
    for j in range(0, i + 1):
        print('* ', end=' ')
    print('\r')

print('**************************************')

'''
*  *  *  *  *
*  *  *  *  
*  *  *  
*  *  
*
'''
for i in range(0, 6):
    for j in range(0, 6 - i):
        print('* ', end=' ')
    print('\r')

print('**************************************')

'''
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  *  
*  *  *  *  *  * 
'''
for i in range(0, 6):
    for j in range(0, i + 1):
        print('* ', end=' ')
    for k in range(0, 6 - i):
        print('* ', end=' ')
    print('\r')

print('**************************************')
'''

          *
        *  *
      *  *  *
    *  *  *  *
  *  *  *  *  *

'''
for i in range(0, 6):
    for j in range(0, 6 - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        print('* ', end=' ')
    print('\r')

print('**************************************')
'''
  *  *  *  *  *  
    *  *  *  *  
      *  *  *  
        *  *  
          * 
'''
for i in range(0, 6):
    for j in range(0, i + 1):
        print(' ', end=' ')
    for k in range(0, 6 - i):
        print('* ', end=' ')
    print('\r')

print('**************************************')

'''
          * 
        * * 
      * * * 
    * * * * 
  * * * * *
'''
for i in range(0, 6):
    for j in range(0, 6 - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        print('*', end=' ')
    print('\r')

print('**************************************')

'''
  * * * * *
    * * * *
      * * *
        * *
          *
'''
for i in range(0, 6):
    for k in range(0, i):
        print(' ', end=' ')
    for j in range(0, 6 - i):
        print('* ', end='')
    print('\r')

print('**************************************')

'''
1 2 3 4 
5 6 7 
8 9 
10 
'''
num = 1
for i in range(0, 4):
    for j in range(0, 4-i):
        print(num, end=' ')
        num += 1
    print("\r")

print('**************************************')

'''
1 
2 2 
3 3 3 
4 4 4 4 
'''
num = 1
for i in range(0, 5):
    for j in range(1, i+1):
        print(i, end=' ')
        num += 1
    print("\r")

print('**************************************')

'''
1 
1 2 
1 2 3 
1 2 3 4  
'''
num = 1
for i in range(0, 5):
    for j in range(1, i+1):
        print(j, end=' ')
        num += 1
    print("\r")
print('**************************************')

'''
  5 10 15 20 
    25 30 35 
      40 45 
        50
'''
num = 1
for i in range(0, 4):
    for k in range(0, i+1):
        print(' ', end=' ')
    for j in range(0, 4 - i):
        print(num * 5, end=' ')
        num += 1
    print('\r')

print('**************************************')

'''
        2 
      2 4 
    2 4 6 
  2 4 6 8
'''
for i in range(0, 4):
    num = 1
    for j in range(0, 4 - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        print(num * 2, end=' ')
        num += 1
    print('\r')

print('**************************************')

'''
        1
      1 2
    1 2 3
  1 2 3 4
'''
for i in range(0, 4):
    num = 1
    for j in range(0, 4 - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        print(num, end=' ')
        num += 1
    print('\r')

print('**************************************')

'''
        1 
      2 3 
    4 5 6 
  7 8 9 10 
'''

num = 1
for i in range(0, 4):
    for j in range(0, 4 - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        print(num, end=' ')
        num += 1
    print('\r')

print('**************************************')

'''
1 0 1 0 
1 0 1 0 
1 0 1 0 
1 0 1 0 
'''
for i in range(0, 4):
    for j in range(0, 2):
        print(1, end=' ')
        print(0, end=' ')
    print("\r")

print('**************************************')

'''
            1  
          2  3  
        4  5  6  
      7  8  9  10  
    11  12  13  14  15 
'''

c = 0
for i in range(0, 5):
    for j in range(0, 6 - i):
        print(' ', end=' ')
    for k in range(0, i + 1):
        c = c + 1
        print(str(c) + " ", end=' ')
    print('\r')

print('**************************************')
