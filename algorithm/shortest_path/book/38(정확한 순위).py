"""
A->B로 가는 길이 있다
: A는 B보다 순위가 높다
C->A로 가는 길이 있다
: C는 A보다 순위가 높다
모든 지점에서 다른 모든 지점 체크해야함 -> 플로이드워셜

"""

import sys
input = sys.stdin.readline
INF = sys.maxsize

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j],G[i][k]+G[k][j])


N,M = map(int,input().split())
G = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s,e = map(int,input().split())
    s,e = s-1,e-1
    G[s][e] = 1 # s->e로 가는 길이 있다.


floyd_warshall()
cnt = 0
for i in range(N):
    for j in range(N):
        """
        i,j 비교
        i->j 로 가는 길이 있다. i는 j보다 순위가 높다
        j->i 로 가는 길이 있다. j는 i보다 순위가 높다
        """
        if i==j:
            continue
        if G[i][j] == INF and G[j][i] == INF: # 순위를 알 수 없음
            break
    else:
        cnt +=1

print(cnt)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4

"""