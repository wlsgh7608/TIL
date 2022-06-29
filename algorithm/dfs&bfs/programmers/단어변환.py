def diff_check(word1,word2):
    diff = 0
    for a,b in zip(word1,word2):
        if a != b:
            diff +=1
    if diff == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    from collections import deque
    Q =  deque()
    cnt = 0
    Q.append((begin,0))
    while Q:
        current,cnt = Q.popleft()
        if current == target:
            return cnt
        if cnt == len(words):
            return 0
        for word in words:
            if diff_check(current,word):
                Q.append((word,cnt+1))
    
    return cnt