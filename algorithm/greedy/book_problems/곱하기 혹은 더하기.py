"""
곱하기 혹은 더하기 / 4분
17:54 ~ 17:58
"""

numbers = input()
numbers = list(map(int,numbers))
result = 0
for n in numbers:
    result = max(result+n,result*n) # 더하기 혹은 곱하기 한 결과중 큰 값
print(result)