"""
https://www.acmicpc.net/problem/2343
기타레슨 / 실버 1 / 
실패 1 
"""

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
records = list(map(int,input().split()))
lo,hi = 1,1_000_000_000
def check(records,blueray,M):
    c_volume= 0 
    cnt =1
    for record in records:
        if record> blueray:
            return False
        if record+c_volume <= blueray:
            c_volume += record
        else:
            c_volume = record
            cnt+=1
    if cnt <= M:
        return True
    else:
        return False

# lower bound    
while lo <= hi:
    m = (lo+hi)//2
    if check(records,m,M):
        hi = m-1
    else:
        lo = m+1
print(lo)