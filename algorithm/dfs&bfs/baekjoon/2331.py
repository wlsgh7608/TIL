"""
https://www.acmicpc.net/problem/2331
반복수열 / 실버 4 / 7분
15:28 ~  15:35

"""


A, P = map(int,input().split())

S = [A]
current = A
while True:
    str_n = str(current)
    value = 0
    for n in str_n:
        value += int(n)**P
    if value in S:
        result = S.index(value)
        break
    else:
        current = value
        S.append(value)

print(result)
