"""
만들 수 없는 금액 / 
16:12 ~ 16:17

"""

n = int(input())
coins = list(map(int,input().split()))
coins.sort()
t = 1

for c in coins:
    if t < c:
        break
    t+=c


print(t)
"""
5
3 2 1 1 9

1 1 2 3 9

target : 1
1만들 수 있음- 1 개
target : 2
1 만들 수 있음 - 1,1

target : 3
만들 수 ㅣㅇ ㅆ음 1,2

target : 5


현재 있는 거 1

1로는 모든 것을 마들 수 있음

다음 1,1

1~2의 숫자를 만들 수 있음

다음 1,1,2

1~4의 숫자를 만들 수 있음

다음 1,1,2,3

1~7의 숫자를 만들 수 있음

다음 1,1,2,3,9

1~7, 9~15의 숫자를 만들 수 있다.

현재 만들 수 있는 숫자보다 큰 수 가 들어올 경우 안됨







"""