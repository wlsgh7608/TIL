"""
https://www.acmicpc.net/problem/9019
DSLR / 골드 4 / 55분 pypy3
09:03 ~  09:58
실패 6(시간초과 4, 메모리초과 1, 런타임 에러 1)
"""
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


def D(n):
    return (2*n)%10000
def S(n):
    return (n-1)%10000
def L(n):
    return (10*n+ n//1000)%10000
def R(n):
    return (n//10 + 1000*(n%10))

dict_cmd = {0:D,1:S,2:L,3:R}

for _ in range(T):
    A,B = map(int,input().split())
    Q = deque()
    visited = [False for _ in range(10000)]
    visited[A] = True
    Q.append([A,''])
    while Q:
        n,cmds = Q.popleft()
        if n == B:
            print(cmds)
            break
        for i in range(4):
            cmd_n = dict_cmd[i](n)
            if not visited[cmd_n]:
                visited[cmd_n] = True
                # cmd + 함수의 이름 추가
                Q.append([cmd_n,cmds+dict_cmd[i].__name__])
