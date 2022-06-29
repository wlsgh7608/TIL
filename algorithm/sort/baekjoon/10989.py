"""
https://www.acmicpc.net/problem/10989
수 정렬하기 3 / 실버 5 / 9분
10:05 ~ 10:14

"""
import sys
input  = sys.stdin.readline

n = int(input())
# count sort
cnt_box  = [0 for _ in range(10001)]
for _ in range(n):
    number = int(input())
    cnt_box[number] +=1


for idx,cnt in enumerate(cnt_box):
    for i in range(cnt):
        print(idx)
    