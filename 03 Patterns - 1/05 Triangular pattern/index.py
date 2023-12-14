'''
    1
    12
    123
    1234
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j = j + 1
    print()
    i = i + 1



'''
    1
    23
    345
    4567
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(i+j-1, end=' ')
        j = j + 1
    print()
    i = i + 1




'''
    1
    23
    456
    78910
'''
n = int(input())
i = 1
k = 1
while i <= n:
    j = 1
    while j <= i:
        print(k, end=' ')
        k = k + 1
        j = j + 1
    print()
    i = i + 1
