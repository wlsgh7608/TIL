"""
https://www.acmicpc.net/problem/2512
예산 / 실버 3 / 12분
9:58 ~ 10:10
"""
import sys
input = sys.stdin.readline
N = int(input())
budgets = list(map(int,input().split()))
M = int(input())
budgets.sort()
lo,hi = 1,budgets[-1]

def check(budgets,value,M):
    possible =[budget if budget<= value else value for budget in budgets]
    if sum(possible)<=M:
        return True
    else:
        return False
    

# upper bound 이용
while lo<= hi:
    m = (lo+hi)//2
    if check(budgets,m,M):
        lo = m+1
    else:
        hi = m-1
print(lo-1)