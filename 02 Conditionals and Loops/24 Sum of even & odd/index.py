N = int(input())
even = 0
odd = 0
while N > 0:
    remainder = N % 10
    N = N // 10
    if remainder % 2 == 0:
        even = even + remainder
    else:
        odd = odd + remainder
print(even, " ", odd)
