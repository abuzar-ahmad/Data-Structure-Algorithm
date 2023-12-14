'''
    1111
    2222
    3333
    4444
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i, end=' ')
        j = j + 1
    print()
    i = i + 1



'''
    1234
    1234
    1234
    1234
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(j, end=' ')
        j = j + 1
    print()
    i = i + 1



'''
    4321
    4321
    4321
    4321
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(n - j + 1, end=' ')
        j = j + 1
    print()
    i = i + 1
