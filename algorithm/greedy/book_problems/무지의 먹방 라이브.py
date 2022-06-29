"""
https://programmers.co.kr/learn/courses/30/lessons/42891
무지의 먹방 라이브

"""

def solution(food_times, k):
    from collections import defaultdict
    # 먹는 시간, 해당 인덱스
    food_dic = {}
    for i,food in enumerate(food_times):
        if food in food_dic:
            food_dic[food].append(i+1)
        else:
            food_dic[food] = [i+1]
    foods_types = sorted(food_dic)
    nums = len(food_times)
    current_t = 0
    p =  0 #food_types 포인터
    if sum(food_times)<=k:
        return -1
    while True:
        min_f = foods_types[p]
        diff = min_f-current_t
        if diff * nums > k:
            break
        k -= diff*nums
        p+=1
        current_t = min_f
        nums -= len(food_dic[min_f])
    remain_foods = [i+1 for i,x in enumerate(food_times) if x>=min_f]
    k = k %len(remain_foods)
    return remain_foods[k]