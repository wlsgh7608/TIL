def solution(n, computers):
    from collections import deque
    not_visited = [True for _ in range(n)]
    
    cnt = 0
    while any(not_visited):
        Q = deque()
        alone = not_visited.index(True)
        Q.append(alone)
        not_visited[alone]  = False
        cnt+=1
        while Q:
            current = Q.popleft()
            for i in range(n):
                if computers[current][i] and not_visited[i]:
                    not_visited[i] = False
                    Q.append(i)
            
            

    return cnt