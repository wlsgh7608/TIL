# https://www.acmicpc.net/problem/11047

n,k = map(int,input().split())
coin_list = []



for _ in range(n):
    coin = int(input())
    coin_list.append(coin)


idx = n-1
cnt = 0
while k:
    # Ai은 Ai-1의 배수임
    coin_cnt = k // coin_list[idx] # 해당 코인으로 나눈 몫
    k %= coin_list[idx] # 해당 코인으로 나눈 나머지
    cnt += coin_cnt # 전체 코인개수에 추가

    idx-=1 # 인덱스 하나씩 줄이기
    

print(cnt)