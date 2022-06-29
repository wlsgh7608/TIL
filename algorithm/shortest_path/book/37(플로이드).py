"""
https://www.acmicpc.net/problem/11404
플로이드 / 골드 5 / 10분
실패1(출력초과 1)
"""
import sys
INF = sys.maxsize
input = sys.stdin.readline

def floyd_warshall():
    for k in range(N): # k: 지나가는 도시
        for i in range(N): # 시작
            for j in range(N): # 끝
                G[i][j] = min(G[i][j],G[i][k]+G[k][j]) # i에서 j를 가는 경우와 i에서 k를 거쳐 j가는 경우 비교

N = int(input())
M = int(input())
G = [[INF for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s,e,w = map(int,input().split())
    s,e = s-1,e-1
    G[s][e] = min(G[s][e],w)

floyd_warshall()

for i in range(N):
    for j in range(N):
        if i==j or G[i][j]== INF:
            print(0,end=" ")
        else:
            print(G[i][j],end=" ")
    print()

