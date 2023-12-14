n = int(input())
d = 2
flag = False
while d < n:
    if (n % d == 0):
        print('n is not prime')
    d = d + 1

if flag:
    print('not prime')
else:
    print('prime')
