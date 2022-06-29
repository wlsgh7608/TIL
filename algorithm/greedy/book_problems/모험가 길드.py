"""
모험가 길드 / 7분
15:36 ~ 15:43

공포도를 기준으로 오름차순으로 정렬 후 해당 값만큼 인덱스 이동 (끝에 도착할 때 까지 반복)
"""
import sys
input = sys.stdin.readline
n = int(input())
peoples = list(map(int,input().split()))
peoples.sort()
cnt = 0
p = 0
while p< len(peoples):
    current = peoples[p]
    p +=current
    if p < len(peoples):
        cnt+=1
        
print(cnt)


"""
input
5
2 3 1 2 2
"""