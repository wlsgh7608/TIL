# 왕실의 나이트
"""
- [✔] 완전탐색(브루트 포스) 
- [✔] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 각각의 이동 경로에 대하여 판의 범위 안에 있는 지 체크
시간복잡도 : O(1)
"""


loc = input()
x = ord(loc[0])- ord('a')
print(x)
y = int(loc[1]) - 1
# 체스판의 범위 : 0 ~ 7

moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

cnt = 0
for move in moves:
    nx = x + move[1]
    ny = y + move[0]
    if nx>=0 and ny>=0  and nx < 8 and ny < 8:
        cnt+=1
print(cnt)

"""
input 
a1

output
2
"""