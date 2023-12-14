'''
    A
    B C
    C D E
    D E F G
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(chr(64+i+j-1), end='')
        j = j + 1
    print()
    i = i + 1
