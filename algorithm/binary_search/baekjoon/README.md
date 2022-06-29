# [1920번 - 수 찾기](https://www.acmicpc.net/problem/1920) 

## 수 찾기 / 실버 4 / 4분

- 일반적인 이진 탐색 문제
- m값이 맞을 경우 리턴
- m값보다 타겟값이 큰 경우 s = m+1
- m값보다 타겟값이 작은 경우 e = m-1 

## 전체코드 

``` python
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))


numbers.sort()

for t in targets:
    s,e = 0,N-1
    while s<=e:
        m = (s+e)//2
        if numbers[m] == t:
            print(1)
            break
        elif numbers[m] < t:
            s = m+1
        else:
            e = m-1
    else:
        print(0)

```


# [10816번 - 숫자 카드 2](https://www.acmicpc.net/problem/10816) 
## 숫자카드 2 / 실버 4 / 75분 
 - 시간초과로 인하여 많은 시간을 들임
 - 질문 중 bisect 라이브러리를 이용하라는 말이 있어 이용
 - bisect_left : 리스트에서 데이터를 삽입할 가장 왼쪽 인덱스를 리턴
 - bisect_right : 리스트에서 데이터를 삽입할 가장 오른쪽 인덱스를 리턴
 - [bisect 설명 사이트](https://heytech.tistory.com/79)

## 오답코드(시간초과)
- 시간초과가 나는 코드

``` python
import sys
input = sys.stdin.readline
def lower_check(s,e):
    ans = -1
    while s<=e:
        m = (s+e)//2
        if numbers[m] == t:
            ans = m
            e = m-1
        elif numbers[m] < t:
            s = m +1
        else:
            e = m-1
    return ans

def upper_check(s,e):
    ans = -1
    while s<=e:
        m = (s+e)//2
        if numbers[m] == t:
            ans = m
            s = m+1
        elif numbers[m] < t:
            s = m +1
        else:
            e = m-1
    return ans
            

N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
targets  = list(map(int,input().split()))
numbers.sort()
for t in targets:
    s = 0
    e = N-1
    up = upper_check(s,e)
    down = lower_check(s,e)
    if up== -1 and down == -1:
        print(0,end=" ")
    else:
        print(up-down+1,end=" ")
```


## 생각해보아야 할 것
- 다음 코드는 시간초과가 나지 않는 코드임
- 왜 시간 초과가 나지 않는 것인지 체크
``` python
import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().rstrip().split()))
qn = int(sys.stdin.readline())
ql = list(map(int,sys.stdin.readline().rstrip().split()))
l.sort()

def upper_bound(start,end,val):
    while(start<end):
        mid = (start+end)//2
        if l[mid] <= val:
            start = mid+1
        else:
            end = mid
    return end
def lower_bound(start,end,val):
    while(start<end):
        mid = (start+end)//2
        if l[mid] < val:
            start = mid+1
        else:
            end = mid
    return end
ans = []
for query in ql:
    ans.append(upper_bound(0,n,query)-lower_bound(0,n,query))
print(*ans)
```


## 전체코드 
``` python
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
            

N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
targets  = list(map(int,input().split()))
numbers.sort()


result = []
for t in targets:
    s = 0
    e = N-1
    up = bisect_right(numbers,t)
    down = bisect_left(numbers,t)
    print(up-down,end=" ")
```

# [1654번 - 랜선 자르기](https://www.acmicpc.net/problem/1654) 
## 랜선 자르기 / 실버 3 / 15분
- 생길 수 있는 가장 짧은 랜선 길이 : 1
- 생길 수 있는 가장 긴 랜선 길이 : lines[-1]
- 따라서 그 중간 값 m을 이용하여 이진 탐색

``` python
s,e = 1,lines[-1]
ans = s
while s<=e:
    m = (s+e)//2
```

# 전체코드 

``` python

import sys
input = sys.stdin.readline
K, N = map(int,input().split())
lines = [int(input()) for _ in range(K)]
lines.sort()

s,e = 1,lines[-1]
ans = s
while s<=e:
    m = (s+e)//2
    numbers = [line//m for line in lines]
    if sum(numbers)>=N:
        ans = m
        s=m+1
    else:
        e= m-1
print(ans)

```

# [2110번 - 공유기 설치](https://www.acmicpc.net/problem/2110) 

## 공유기 설치 / 골드 5 / 62분
- 생각을 달리 해봐야 풀리는 이진탐색 문제
- 거리를 기준으로 했을 때 공유기 개수를 이용하여 이진탐색 실행
- 가장짧은 거리 : 1 , 가장 긴 거리 : houses[-1]
``` python
min_d,max_d = 0,houses[-1]
```

- 중간 거리를 이용하여 공유기 개수 체크
- 최근에 공유기가 설치된 집을 기준으로 거리이상 차이날 시 공유기 추가
``` python
def check(houses,distance):
    current = houses[0] 
    cnt = 1
    for house in houses:
        if house - current >= distance:
            cnt+=1
            current = house
    return cnt
```
- 현재 거리를 기준으로 공유기 개수가 같거나 많을 경우 거리를 늘림(공유기 개수를 줄이기 위해)
- 개수가 적을 경우 거리를 줄여야 함(공유기 개수를 늘리기 위해)

``` python
if check(houses,d)>=C: # 공유기 개수가 같거나 많을 시 거리를 늘려야 함
        ans = d
        min_d=d+1
else: # 공유기 개수가 작을 시 거리를 줄여야함
    max_d = d-1

```

## 전체코드 

``` python


def check(houses,distance):
    current = houses[0] 
    cnt = 1
    for house in houses:
        if house - current >= distance:
            cnt+=1
            current = house
    return cnt

import sys
input = sys.stdin.readline
N, C = map(int,input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
min_d,max_d = 0,houses[-1]
while min_d<=max_d:
    d = (min_d+max_d)//2
    if check(houses,d)>=C: # 공유기 개수가 같거나 많을 시 거리를 늘려야 함
        ans = d
        min_d=d+1
    else: # 공유기 개수가 작을 시 거리를 줄여야함
        max_d = d-1
print(ans)

```