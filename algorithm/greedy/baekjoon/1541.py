"""
https://www.acmicpc.net/problem/1541

### 체크리스트
- [X] 현재 상황에서 가장 좋은 것만 고르는가? 
 결과 : '-' 이전 모든 숫자의 합 - '-' 이후의 모든 숫자의 합
- [X] 해당 해법이 정당한가? 
 연산자는 연속적으로 사용하지 않음
 a - b +c -d 의 경우 a - (b+c)-d로 괄호를 묶을 수 있음

input
55-50+40

output
-35

input
10+20+30+40

output
100

input 
00009-00009

output
0
"""

input_list = input()
try:
    first_minus = input_list.index('-')
except:
    first_minus = len(input_list)

pre_str = input_list[:first_minus]
post_str = input_list[first_minus+1:]
pre_str = pre_str.replace('-','+')
post_str = post_str.replace('-','+')

pre_sum = 0
post_sum = 0
if pre_str:
    pre_sum = sum(list(map(int,pre_str.split('+'))))

if post_str:
    post_sum = sum(list(map(int,post_str.split('+'))))

print(pre_sum - post_sum)