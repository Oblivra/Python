'''

    *
   ***
  *****
 *******
*********

'''

# for i in range(1, 6):
#     print(' ' * (5 - i) + '*' * (2*i - 1))

# n = 5
# for i in range(1, n+1):
#     for j in range(n - i):
#         print(' ', end='')
#     for k in range(2 * i - 1):
#         print('*', end='')
#     print()


def diamond(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * (2*i - 1))
    for i in range(n-1, -1, -1):
        print(' ' * (n-i) + '*' * (2*i - 1))

diamond(5)