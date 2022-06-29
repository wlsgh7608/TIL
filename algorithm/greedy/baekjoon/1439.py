"""
https://www.acmicpc.net/problem/1439
### 체크리스트
- [✔] 현재 상황에서 가장 좋은 것만 고르는가? 
    - 0과 1의 연속중 적은 것을 뒤집으면 됨 
- [✔] 해당 해법이 정당한가? 
    - 01010100101010
    - 00101011010100
    - 00010100101000
    - 00001011010000
    - 00000100100000
    - 00000011000000
    - 00000000000000 

"""

inp = input()
current =inp[0]

c_0 = 0
c_1 = 0
if current == '0':
    c_0+=1
else:
    c_1+=1

for i in inp:
    if i == current:
        continue
    else:
        current = i
        if i =='0':
            c_0+=1
        else:
            c_1 +=1
            
print(min(c_0,c_1))