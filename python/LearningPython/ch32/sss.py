def solution(grid, k):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_moves = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    max_moves[0][0] = k
    D = [(-1,0),(0,-1),(1,0),(0,1)]
    import heapq

    Q = []
    heapq.heappush(Q,(0,0,0,k)) # cnt,x,y,moves
    while Q:
        cnt,x,y,moves = heapq.heappop(Q)
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            print(nx,ny)
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]and max_moves[nx][ny]<moves-1:
                    if grid[nx][ny] == 'F':
                        heapq.heappush(Q,(cnt,nx,ny,moves-1))
                        max_moves[nx][ny] = moves-1
                    elif grid[nx][ny] == '.':
                        heapq.heappush(Q,(cnt,nx,ny,moves-1))
                        heapq.heappush(Q,(cnt+1,nx,ny,k))
                        max_moves[nx][ny] = k
                if not visited[nx][ny] and moves:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 'F':
                        heapq.heappush(Q,(cnt,nx,ny,moves-1))
                        max_moves[nx][ny] = max(max_moves[nx][ny],max_moves[x][y]-1)
                    elif grid[nx][ny] == '.':
                        heapq.heappush(Q,(cnt,nx,ny,moves-1))
                        heapq.heappush(Q,(cnt+1,nx,ny,k))
                        max_moves[nx][ny] = max(max_moves[nx][ny],k)

grid = [".FFFF.", "####F#", "####F#", "####FF"]
k = 7
solution(grid,k)