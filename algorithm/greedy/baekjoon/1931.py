# https://www.acmicpc.net/problem/1931

"""
input
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

output



"""

def solve1():
    """
    ### 체크리스트
    - [X] 현재 상황에서 가장 좋은 것만 고르는가? 
      - 시작시간과 종료시간을 선으로 연결 했을 때 곂치지 않는 선의 개수

    - [ ] 해당 해법이 정당한가? 
      - LIS을 이용하게 될 경우 O(n^2)의 시간복잡도 발생 - for문 계산
      - 입력값은 100_000일 경우 100억의 계산 : 약 100초

    """


    n = int(input())



    board = []
    for _ in range(n):
        s,e = map(int,input().split())
        board.append((s,e))



    board.sort(key = lambda x:(x[1],x[0])) # 종료시간, 시작시간 sort
    # LIS 
    dp = [1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if board[i][0] >= board[j][1] :
                dp[i] = max(dp[i],dp[j]+1)
    print(dp)
    print(dp[-1])

def solve2():
    """
    ### 체크리스트
    - [X] 현재 상황에서 가장 좋은 것만 고르는가? 
        - 시작시간과 종료시간을 정렬한 뒤 가장 작은 종료시간을 기준으로 선택
    - [X] 해당 해법이 정당한가? 
        - 가장 작은 종료시간을 기준으로 회의실을 잡는 것은 바람직

    시간복잡도 : O(nlogn)- sort

    """
    n = int(input())
    board = []
    for _ in range(n):
        s,e = map(int,input().split())
        board.append((s,e))

    board.sort(key = lambda x:(x[1],x[0])) # 종료시간, 시작시간 sort
    for i,(s,e) in enumerate(board):
        if i==0:
            end = e
            cnt = 1
            continue
        if s>= end:
            end = e # 최근 끝난 회의실 시각 update
            cnt += 1
        
    print(cnt)

solve2()