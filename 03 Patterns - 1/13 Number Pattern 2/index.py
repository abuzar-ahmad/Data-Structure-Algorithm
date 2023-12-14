'''
    1
    1 1
    2 0 2
    3 0 0 3
'''
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if i == 1:
            print(1, end='')
        elif j == 1 or j == i:
            print(i-1, end=' ')
        else:
            print(0, end=' ')
        j = j + 1
    print()
    i = i + 1 
