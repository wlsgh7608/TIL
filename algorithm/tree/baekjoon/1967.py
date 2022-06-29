import sys
input  = sys.stdin.readline




n = int(input())
G = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))
def bfs(node):
    from collections import deque
    visited = [False for _ in range(n+1)]
    Q = deque()
    Q.append((node,0))
    visited[node] = True
    max_len,max_city = [0,0]

    while Q:
        current, dist = Q.popleft()

        for next,extra_dist in G[current]:
            if not visited[next]:
                visited[next] = True
                if dist+extra_dist > max_len:
                    max_len = dist+extra_dist
                    max_city = next
                Q.append((next,dist+extra_dist))
    return max_len,max_city

_,next = bfs(1)
result,_ = bfs(next)
print(result)




    

