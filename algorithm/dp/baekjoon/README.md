
# [피보나치 함수](https://www.acmicpc.net/problem/1003)
## 피보나치 함수 / 실버 3 / 5분
- 피보나치의 작동원리를 생각해보면 쉽게 풀 수 있음
``` python
f[n] = f[n-1] + f[n-2](n>=2)
```
- 따라서 0의 호출은 `dp[i][0] = dp[i-1][0] + dp[i-2][0]`
- 1의 호출은 `dp[i][1] = dp[i][1] = dp[i-1][1] + dp[i-2][1]`


## 전체 코드
``` python
import sys
input = sys.stdin.readline
dp = [[0,0] for _ in range(41)] # 0<=n<=40
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]


n = int(input())

for _ in range(n):
    number = int(input())
    print(*dp[number])

```
# [계단 오르기](https://www.acmicpc.net/problem/2579)
## 계단 오르기 / 실버 3 / 15분
## 실패 1(런타임 에러)
- 런타임 에러가 났던 이유
``` python
dp[1] = steps[1]
dp[2] = steps[1]+steps[2]
```
계단이 1개인 경우 인덱스 에러가 발생하므로 다음과 같이 코드 수정
``` python
dp[1] = steps[1]
if len(steps)>2:
    dp[2] = steps[1]+steps[2]
```

- 현재의 계단을 건널 수 있는 경우의 수 ]
   - `2개, 1개` 건넌 뒤 `1개` 건너는 경우 
   - `2개` 건너는 경우
 ``` python
    two_step = dp[i-2] + steps[i] 
    one_step = dp[i-3] + steps[i-1] + steps[i]
    dp[i] = max(one_step,two_step)
 ```
## 전체 코드
``` python
import sys
input = sys.stdin.readline

iter = int(input())
steps = [0]
for _ in range(iter):
    step = int(input())
    steps.append(step)

dp = [0 for _ in range(len(steps))]
dp[1] = steps[1]
if len(steps)>2:
    dp[2] = steps[1]+steps[2]
for i in range(3,len(steps)):
    two_step = dp[i-2] + steps[i] 
    one_step = dp[i-3] + steps[i-1] + steps[i]
    dp[i] = max(one_step,two_step)
print(dp[-1])
```

# [포도주 시식](https://www.acmicpc.net/problem/2156)
## 포도주 시식 / 실버 1 / 8분
- 현재 상황(`i`)에서의 최대 경우
   - `i-1`번째 포도주의 경우 = `dp[i-1]`
   - `i-2`번째의 포도주 경우와 `i`번째 포도주를 마신 경우 = `dp[i-2] + grapes[i]`
   - `i-3`번째의 포도주 경우와 `i-1`번째, `i`번째 포도주를 마신 경우 = dp[i-3]+grapes[i-1]+grapes[i]
## 전체 코드
``` python
import sys
input = sys.stdin.readline


n = int(input())
grapes = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    if i < 2:
        dp[i] = dp[i-1] + grapes[i]
    else:
        dp[i] = max(dp[i-1],dp[i-2]+grapes[i], dp[i-3]+grapes[i-1]+grapes[i])
    
print(dp[-1])
```
# [평범한 배낭](https://www.acmicpc.net/problem/12865)
## 평범한 배낭 / 골드 5 / 14분
- 가방무게를 dp로 두고 계산하여 풀 수 있음
- `dp = [0 for _ in range(K+1)]`
- 현재 상황에서의 최대 가치를 계산하는 방법
   - 현재 무게의 가치(`dp[i]`)와 현재 무게에서 물품의 무게를 뺀 가치(`dp[i-w]`)에서 물품의 무게(`w`)을 더한 값 비교 
 ``` python
 dp[i] = max(dp[i],dp[i-w]+v)
 ```
- 반복문을 반대로 돌려야 현재 물품의 무게가 계속 업데이트 되는 상황을 피할 수 있음

## 전체 코드
``` python
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
dp = [0 for _ in range(K+1)]
for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])
```