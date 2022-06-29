import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
    def dfs(s,uses,ans):
        if all(uses):
            return ans

        for idx,use in enumerate(uses):
            if not use and tickets[idx][0] == s :
                new_uses = uses[:]
                new_ans = ans[:]
                s,e = tickets[idx]
                new_uses[idx] = True
                new_ans.append(e)
                result = dfs(e,new_uses,new_ans)
                if result:
                    return result 
        return 
    tickets.sort()
    
    start = 'ICN'
    is_use = [False for _ in range(len(tickets))]
    ans = dfs('ICN',is_use,['ICN'])
    return ans