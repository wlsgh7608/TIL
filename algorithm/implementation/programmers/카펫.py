"""
- [✔] 완전탐색(브루트 포스) 
- [ ] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 1 ~ n 제곱근중 약수인지(나누어떨어지는지) 판별
  - 이후 갈색넓이:(x+2)*2+2*y와 brown 값이 같은지 판별
"""
def solution(brown,yellow):
    pos_list = []
    for i in range(1,int(yellow**(1/2))+1):
        if yellow %i == 0:
            x,y = yellow//i , i
            if (x+2)*2 + 2*y == brown:
                return [x+2,y+2]

def wrong_solution(brown, yellow):
    # 시간초과 발생
    pos_ylist = []
    for i in range(1,yellow+1):
        for j in range(1,i+1):
            if i*j == yellow:
                pos_ylist.append((i,j))
    # yellow (i,j)일 때 brown = (i+1)*2 +2*j
    for pos_y in pos_ylist:
        x,y = pos_y
        if (x+2)*2+2*y == brown:
            return ([x+2,y+2])