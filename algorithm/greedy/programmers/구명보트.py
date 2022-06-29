def wrong_solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    cnt = 0
    not_rescure = [True for _ in range(len(people))]
    
    sec_idx = 0
    # 무거운 사람 먼저
    while True in not_rescure: #O(n)
        idx = not_rescure.index(True)
        cur_limit = limit - people[idx]
        not_rescure[idx]  = False
        
        idx+=1
        while idx < len(people): #O(n)
            if not_rescure[idx] and people[idx] <= cur_limit:
                cur_limit -= people[idx]
                not_rescure[idx] = False
            idx+=1
        cnt+=1
    return cnt


def solution(people, limit):
    
    people.sort(reverse=True) # 내림차순
    cnt = 0
    i = 0 # 가장 무거운 사람
    j = len(people) - 1  # 가장 가벼운 사람
    
    # 무거운 사람 먼저
    while i<=j:
        if i==j: # 혼자 남을 경우
            cnt+=1
            break
        if people[i]+people[j]<=limit: # 같이 태울 수 있는 경우
            i+=1
            j-=1
            cnt+=1
        else: # 같이 못태울 경우 ( 무거운 사람만 태움)
            i+=1
            cnt+=1
            
    return cnt


