'''
    1
    1 1
    1 2 1
    1 2 2 1
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if i == 1:
            print(1, end=' ')
        elif j == 1 or j == i:
            print(1, end=' ')
        else:
            print(2, end=' ')
        j = j + 1
    print()
    i = i + 1
