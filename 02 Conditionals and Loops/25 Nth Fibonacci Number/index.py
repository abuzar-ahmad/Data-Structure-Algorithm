N = int(input())
N1 = 0
N2 = 1
i = 1
if(N == 1):
    print(1)
else:
    while(i < N):
        Nth = N1 + N2
        N1 = N2
        N2 = Nth
        i += 1
    print(Nth)
