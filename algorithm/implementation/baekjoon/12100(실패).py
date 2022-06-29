
import sys



input = sys.stdin.readline
N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]
from copy import deepcopy

# 4^5
# 16*16*4

def dfs(level,G):
    if level==5:
        return


def up(G):
    G = deepcopy(G)
    for j in range(N):
        current = 0
        for i in range(1,N):
            if G[i][j]:
                # current값 없을 때
                if not G[current][j]:
                    G[current][j] = G[i][j]
                    G[i][j] = 0
                # current 값과 일치 => current 값 2배 , 인덱스+1
                elif G[current][j] == G[i][j]:
                    G[current][j] =G[current][j]*2
                    G[i][j] = 0
                    current+=1
                else:
                    current+=1
                    # G[current][j] = G[i][j]
                    # G[i][j] = 0
                    
    for row in G:
        print(row)
    return G
def down():
    pass

def right():
    pass

def left(G):
    G = deepcopy(G)
    for i in range(N):
        current = 0
        for j in range(1,N):
            if G[i][j]:
                # current값 없을 때
                if not G[i][current]:
                    G[i][current] = G[i][j]
                    G[i][j] = 0
                    # current+=1
                # current 값과 일치 => current 값 2배 , 인덱스+1
                elif G[i][current] == G[i][j]:
                    G[i][current] =G[i][current]*2
                    G[i][j] = 0
                    current+=1
                else:
                    current= j
                    # G[i][current] = G[i][j]
                    # G[i][j] = 0
    for row in G:
        print(row)
    return G
new = left(G)
print()
nnew = left(new)
"""
4
2 4 2 2
4 4 4 4
8 8 8 4
2 0 8 2

4
2 4 2 2
4 4 4 4
8 4 8 4
2 4 8 2


"""