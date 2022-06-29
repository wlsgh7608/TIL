"""
https://www.acmicpc.net/problem/1525
퍼즐 / 골드2 / 82분 
11:00 ~ 12:22
"""

import sys
input = sys.stdin.readline
from collections import deque


def bfs():

    while Q:
        (x,y),puzzles,cnt = Q.popleft()
        if puzzles == answer:
            return cnt

        for dx,dy in zip(X,Y):
            nx ,ny = x+dx,y+dy
            if 0<=nx<3 and 0<=ny <3 :
                n_p = puzzles[:]
                n_p = list(n_p)
                n_p[3*nx+ny],n_p[3*x+y] = n_p[3*x+y] ,n_p[3*nx+ny]
                str_l = ''.join(n_p)
                if not visited_dict.get(str_l):
                    visited_dict[str_l] = 1
                    Q.append(((nx,ny),str_l,cnt+1))
    return -1


G =""
for _ in range(3):
    row = input().split()
    row = ''.join(row)
    G+=row

visited_dict = {}

Q = deque()
X = [0,0,-1,1]
Y = [-1,1,0,0]
answer = "123456780"
for i in range(9):
    if G[i] == '0':
        zero_idx = i
        break
Q.append(((zero_idx//3,zero_idx%3),G,0))
print(bfs())



