# 1이 될 때 까지
"""
### 체크리스트
- [X] 현재 상황에서 가장 좋은 것만 고르는가? 
  - 나누어 떨어지는 경우를 찾음
- [X] 해당 해법이 정당한가? 
  - 나누어 떨어졌을 때는 1씩 뺄때보다 횟수가 작거나 같음
  - n의 연산은 1씩빼거나, k로 나누거나 밖에 없음


시간복잡도 : O(logk(n))
"""

n,k = map(int,input().split())
cnt = 0

while n != 1:
    if n%k ==0:
        n = n//k
    else:
        n -=1
    cnt+=1
print(cnt)
"""
input
25 5

output 
2

"""