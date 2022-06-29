N,M = map(int,input().split())
E = []
for _ in range(M):
    s,e,v = map(int,input().split())
    E.append((v,s,e))
parent = [i for  i in range(N)]

def find_parent(v):
    if parent[v] != v:
        parent[v] = find_parent(parent[v])
    return parent[v]
def union(a,b):
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



E.sort()
result = 0
check = 0
for v,s,e in E:
    r_s = find_parent(s)
    r_e = find_parent(e)
    if r_s != r_e:
        union(r_s,r_e)
    else:
        result+=v
    
print(result)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11 


"""