"""
https://www.acmicpc.net/problem/1439
뒤집기 / 실버 5 / 10분
15:59 ~ 16:09

"""

cards = input()
check = cards[0]
one_check = 0
zero_check = 0
if check=='1':
    one_check+=1
else:
    zero_check+=1

for card in cards[1:]: # 두 번째 카드부터 체크
    if card == check:  # 이전 카드와 같으면 패스
        continue
    else:
        if card == '1': # 다를 경우 해당 카드check +1 , check값 할당
            one_check+=1
        else:
            zero_check+=1
        check = card

print(min(one_check,zero_check))
