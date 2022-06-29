def dfs(l,s,numbers,target):
    n = len(numbers)
    cnt = 0
    if l == n :
        if s == target:
            return 1
        else:
            return 0
    cnt+=dfs(l+1,s+numbers[l],numbers,target)
    cnt+=dfs(l+1,s-numbers[l],numbers,target)
    return cnt


def solution(numbers, target):
    answer = dfs(0,0,numbers,target)
    return answer