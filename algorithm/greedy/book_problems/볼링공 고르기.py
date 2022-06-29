"""
볼링공 고르기 / 4분
16:18 ~ 16:22
""" 

N,M = map(int,input().split())
balls = list(map(int,input().split()))
ball_dic = {}
for ball in balls:
    if ball not in ball_dic:
        ball_dic[ball]= 0
    ball_dic[ball]+=1
cnt=0


result = 0
for ball in ball_dic:
    cnt = ball_dic[ball] *(N-ball_dic[ball])
    result+= cnt

print(result//2)
