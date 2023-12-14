n = int(input())

if n % 2 == 0:
    print('n is even')
    if n == 0:
        print('n is zero')
else:
    print('n is odd')


#################################################
n = int(input())
m = int(input())

if n % 2 == 0:
    if m % 2 == 0:
        print('1')
    else:
        print('2')
else:
    print('3')
