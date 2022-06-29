# 숫자 카드 게임
"""
### 체크리스트
- [X] 현재 상황에서 가장 좋은 것만 고르는가? 
  - 각 행별로 가장 작은 값들중 가장 큰 값 선택
- [X] 해당 해법이 정당한가? 
  - 행별로 가장 작은 값들중 가장 큰 값을 선택하므로 정당함
  - 입력 값은 1~10000이므로 최대값을 0으로 초기화하는 것은 정당함

시간복잡도 : O(nm) 
"""

n, m = map(int,input().split())
n_list = []
for _ in range(n):
    n_list.append(list(map(int,input().split())))
max_row = 0

for row in n_list:
    if max_row < min(row):
        max_row = min(row)

print(max_row)

"""

input
3 3
3 1 2
4 1 4
2 2 2

output 
2

input
2 4
7 3 1 8
3 3 3 4

"""

