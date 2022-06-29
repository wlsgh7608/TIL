"""
- [✔] 완전탐색(브루트 포스) 
- [ ] 시뮬레이션 
- [✔] 알고리즘을 어떻게 구현하였는가?
  - 숫자카드들로 순열을 이용하여 소수인지 판별
"""
def is_prime(number):
    if number <2:
        return False
    for i in range(2,int(number**(1/2))+1):
        if number%i == 0:
            return False
    return True

def solution(numbers):
    from itertools import permutations
    num_set = set()
    for i in range(1,len(numbers)+1):
        num_per = list(permutations(numbers,i))
        for current in num_per:
            str_num = ''
            for n in current:
                str_num+=n
            num_set.add(int(str_num))
    cnt = 0
    for pred in num_set:
        if is_prime(pred):
            cnt+=1 
    
    return cnt