"""
- [✔] 현재 상황에서 가장 좋은 것만 고르는가? 
- [✔] 해당 해법이 정당한가? 
시간복잡도 - 
"""
n = int(input())
money_list = []
for _ in range(n):
    money_list.append(int(input())) 



coins = [25,10,5,1]
"""
30 
1 0 1 0
0 3 0 0

40
1 1 1 0
0 4 0 0

50
2 0 0 0
0 5 0 0
"""



for money in money_list:
    remain = money
    c_return = []
    # 25 ,10
    while money:
        for coin in coins:
            share = money//coin
            c_return.append(share)
            money = money%coin

    print(*c_return)

