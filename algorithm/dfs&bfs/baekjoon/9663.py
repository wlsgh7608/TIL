"""
https://www.acmicpc.net/problem/9663
N-Queen / 골드 5 / 37분 (pypy3)

10:18 ~ 10:55

"""
def check(level):
    for i in range(level):
        if G[i] == G[level] or abs(G[i]-G[level]) == abs(i-level):
            return False
    return True

def dfs(level):
    global cnt
    if level == n:
        cnt+=1
        return
    for i in range(n):
        G[level] = i
        if check(level):
            dfs(level+1)



n = int(input())
G = [-1 for _ in range(n)]
cnt = 0
dfs(0)
print(cnt)