# 다이나믹 프로그래밍
## Dynamic Programming(DP)

### 메모리 공간을 약간 더 사용하여 연삭 속도를 비약적으로 증가

# DP 문제 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
## **메모라이제이션(Memorization)** 기법을 사용하여 작은 문제에서 구한 정답을 저장

## ex) 피보나치 수열
- 피보나치 수열은 이전 두 항의 합을 현재의 항으로 설정하는 특징이 있는 수열
- f(n) = f(n-1) + f(n-2)
<img src= "https://www.google.com/url?sa=i&url=https%3A%2F%2Fstevenschmatz.github.io%2Fblog%2F2017%2F12%2F06%2Fintroduction-to-dynamic-programming%2F&psig=AOvVaw3-APW1BaFOaRqcqCdfyW7m&ust=1649673249540000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCKCM__OlifcCFQAAAAAdAAAAABAD">


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