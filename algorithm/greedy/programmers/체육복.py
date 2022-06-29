"""
https://programmers.co.kr/learn/courses/30/lessons/42862
### 체크리스트
- [✔] 현재 상황에서 가장 좋은 것만 고르는가? 
    - 체육복이 없는 사람에 대하여 자기자신,한 치수 큰 사람, 한 치수 작은 사람 에 대하여 조사
- [✔] 해당 해법이 정당한가? 
  - 치수가 작은 사람부터 시작하여 해당 사람보다 한 치수 작은 사람 -> 한 치수 큰 사람이 있는지 조사하고
  - 있을 경우 reserve 집합에서 제거하므로 정당함
시간복잡도 - O(n^2)
"""

def solution(n, lost, reserve):
    # lost,reserve 리스트를 오름차순으로 정렬
    

    """
    same = []
    for _l in lost:
        if _l in reserve:
            same.append(_l)

    for _s in same:
        lost.remove(_s)
        reserve.remove(_s)
    
    중복 제거 
    실행시간 O(len(lost)*len(reserve)) -> O(n^2)

    """

    # set 자료형 이용
    """
    set() - O(s)
    차집합 - O(s1+s2)
    """
    
    
    l_set = set(lost)
    r_set = set(reserve)

    lost,reserve = l_set-r_set, r_set-l_set


    total = n-len(lost) # 체육복챙긴 학생
    asc_lost = sorted(lost) # 오름차순 정렬 -> O(nlogn)
    for l in asc_lost:
        if l-1 in reserve:
            total+=1
            reserve.remove(l-1)
            
        elif l+1 in reserve:
            total+=1
            reserve.remove(l+1)

    return total