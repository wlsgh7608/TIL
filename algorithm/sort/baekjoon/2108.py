"""
https://www.acmicpc.net/problem/2108
통계학 / 실버 3 / 37분 
10:20 ~ 10:57
"""
import sys
input = sys.stdin.readline

n = int(input())
# count sort
cnt_box = [0 for _ in range(8001)] # -4000 ~ 4000
n_list= []
for _ in range(n):
    number = int(input())
    cnt_box[number+4000] +=1

max_idx = 0
is_only = True
for idx,cnt in enumerate(cnt_box):
    for i in range(cnt):
        n_list.append(idx-4000)

    # 최빈값 탐색
    # max_idx =0 으로 초기화 했기 때문에 idx=1부터 탐색 
    if idx>0:
        if cnt > cnt_box[max_idx]:
            max_idx = idx
            is_only = True
        elif cnt == cnt_box[max_idx] and is_only:
            max_idx = idx
            is_only = False

mid = n//2
print(round(sum(n_list)/n))
print(n_list[mid])
print(max_idx-4000)
print(n_list[-1]- n_list[0])
"""
input
3
4000
20
1

output
1340
4000
20
3999

answer
1340
20
20
3999
5
-4000
-3999
-3999
-4000
-1
"""