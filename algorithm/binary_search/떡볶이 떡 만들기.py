
def check(rices,m,M):
    tot = 0
    for rice in rices:
        if rice > m:
            tot += rice-m
    
    if tot <= M:
        return True
    else:
        False

N,M = map(int,input().split())
rices = list(map(int,input().split()))
rices.sort()
s,e = 0,rices[-1]


while s<e:
    m = (s+e)//2
    if check(rices,m,M): # lower bound 구해야함 
        ans = m
        e=m
    else:
        s = m+1
print(e)
"""
4 6 
19 15 10 17

"""