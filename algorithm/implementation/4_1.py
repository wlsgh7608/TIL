# 상하좌우
"""
- [ ] 완전탐색(브루트 포스) 
- [✔] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 주어진 계획서 내용을 차례대로 수행하였다. 

시간복잡도 : O(n)
"""

N = int(input())
plans = list(input().split())
dic = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}
y,x = 1,1
# 범위 : x>0, y>0
for plan in plans:
    mo_y,mo_x = y+ dic[plan][0], x+dic[plan][1]
    if mo_x and mo_y and mo_x< N  and mo_y < N:
        y = mo_y
        x = mo_x
print(y,x)

"""
input
5
R R R U D D

output 
3 4 
"""


# 시각
"""
- [✔] 완전탐색(브루트 포스) 
- [ ] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 모든 시간에 대하여 3이 들어가는지 체크

시간복잡도 : O(h*60*60) = O(h)
"""
n = int(input())

cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            clock = str(h)+str(m)+str(s)
            if '3' in clock:
                cnt +=1

print(cnt)