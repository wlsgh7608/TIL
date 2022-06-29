"""
https://www.acmicpc.net/problem/2263
"""

import sys
input = sys.stdin.readline



n = int(input())
inorders = list(map(int,input().split()))
postorders = list(map(int,input().split()))

print(inorders)
print(postorders)

p,q = 0,0
results = []


def preoder(node):
    print(node)
    left,right = trees[node]
    print(node,end= '')
    if left !=  -1:
        preorder(left)
    if right != -1:
        preorder(right)


"""
4251637
4526731
"""




