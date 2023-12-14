'''
    A B C D
    A B C D
    A B C D
    A B C D
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(chr(64 + j), end=' ')
        j = j + 1
    print()
    i = i + 1





'''
    A B C D
    B C D E
    C D E F
    D E F G
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(chr(64+i+j-1), end=' ')
        j = j + 1
    print()
    i = i + 1
