'''
    E
    D E
    C D E
    B C D E
    A B C D E
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(chr(64-i+j+n), end='')
        j = j + 1
    print()
    i = i + 1
