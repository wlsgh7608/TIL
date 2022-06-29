"""
https://www.acmicpc.net/problem/5582
공통 부분 문자열 / 골드 5
"""
A = input()
B = input()


p = 0
q = 0
ans = ''
while p < len(A):
    word = B[p:q+1]
    if word in A and len(word)> len(ans):
        ans = word
    if p == q:
        q+=1
    elif word in A and q<len(B):
        q+=1
    else:
        p+=1





print(len(ans))