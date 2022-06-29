def solution(routes):
    point_list = set()
    answer = 0 
    routes.sort(key = lambda x: x[1])
    e = -300001
    for route in routes:
        if e<route[0]:
            print(e,"설치")
            answer+=1
            e = route[1]
    return answer