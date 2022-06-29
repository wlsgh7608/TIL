# 큰 수의 법칙
"""
### 체크리스트
- [X] 현재 상황에서 가장 좋은 것만 고르는가? 
  - 수 많은 수 중에서 가장 큰 수와 그 다음 수를 사용한다
  - k번 만큼 가장 큰 수를 사용하고 다음 큰 수를 사용을 반복
- [X] 해당 해법이 정당한가? 
  - 입력 값에 숫자는 최소 2개의 숫자를 입력받음


"""
def solve1():
    """
    시간복잡도 : O(nlogn + m)
    """
    n,m,k = map(int,input().split())
    numbers = list(map(int,input().split()))

    numbers.sort()
    max_n,sec_n = numbers[-1],numbers[-2] # 가장 큰 것, 2번 째로 큰 것

    ans = 0
    k_cnt= 0
    for i in range(m):
        k_cnt+=1

        if k_cnt== k+1: # k번쨰
            ans+=sec_n
        else:
            ans+=max_n
        k_cnt = (k_cnt)%(k+1) # 0,1,2,..,k,0,1,2,..,k
    print(ans)

def solve2():
    """
    반복 되는 수열을 이용한다.
    실행속도를 매우 낮춰줌
    시간복잡도 : O(nlogn) - sort
    """
    n,m,k = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()
    max_n,sec_n = data[-1],data[-2]
    # 3 번의 사용 가능 할 때 m m m n m m m n 반복
    iter_n = m//(k+1)
    remain = m%(k+1)

    ans = iter_n*(max_n*k+sec_n) # 반복수열의 반복 횟수
    ans += remain*max_n # 나머지 : 나머지는 가장 큰 수들로만 이루어짐
    print(ans)

solve2()

"""
input 
5 8 3
2 4 5 4 6
"""