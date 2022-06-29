## [2751번 - 수 정렬하기 2](https://www.acmicpc.net/problem/2751) 

 - 내부 라이브러리 sort(tim sort) 이용 - O(nlogn)
 ``` python
# 내부 sort 이용(tim sort)
numbers.sort()
 ```

 ## 전체코드 

``` python
import sys
input = sys.stdin.readline
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# 내부 sort 이용(tim sort)
numbers.sort()
for i in numbers:
    print(i)
```

# [10989번 - 수 정렬하기 3](https://www.acmicpc.net/problem/10989)

- 수 정렬하기 3 / 실버 5 / 9분
- n의 값이 작은 범위 (1~10000)이므로 count sort 이용 
- count sort의 시간복잡도 O(n+k) (k = 10000)
- count sort은 숫자별 count을 담은 뒤 작은 숫자부터 count 만큼  출력

### count box 에 담기
``` python
cnt_box  = [0 for _ in range(10001)]
for _ in range(n):
    number = int(input())
    cnt_box[number] +=1
```
### 작은 숫자부터 count 만큼  출력
```python
for idx,cnt in enumerate(cnt_box):
    for i in range(cnt):
        print(idx)

```

## 전체코드

``` python
import sys
input  = sys.stdin.readline

n = int(input())
# count sort
cnt_box  = [0 for _ in range(10001)]
for _ in range(n):
    number = int(input())
    cnt_box[number] +=1


for idx,cnt in enumerate(cnt_box):
    for i in range(cnt):
        print(idx)
    
```

# [2108 - 통계학](https://www.acmicpc.net/problem/2108)

 - 통계학 / 실버 3 / 37분 
 - 코드의 틀린 부분을 찾느라 오래걸렸음
## 오답노트
``` python
max_idx = 0
is_only = True
for idx,cnt in enumerate(cnt_box):
    for i in range(cnt):
        n_list.append(idx-4000)

    if cnt > cnt_box[max_idx]:
        max_idx = idx
        is_only = True
    elif cnt == cnt_box[max_idx] and is_only:
        max_idx = idx
        is_only = False
```
### __해당 코드의 경우 최대 인덱스를 0으로 초기화를 했기 때문에 0부터 순차적으로 루프를 돌 시 문제 발생__

ex ) list = [1,2,3] 
 - case 1 
   - 1은 elif 조건절을 만족
   - max_idx = 0, is_only = True
 - case 2,3
   - 어떠한 조건절도 만족하지 않음
** 결과 : 최빈값 1, 정답 : 최빈값 2 **

따라서 두번째 인덱스(idx = 1 )부터 루프를 돌아야 함

## 정답 코드

``` python
import sys
input = sys.stdin.readline

n = int(input())
# count sort
cnt_box = [0 for _ in range(8001)] # -4000 ~ 4000
n_list= []
for _ in range(n):
    number = int(input())
    cnt_box[number+4000] +=1

max_idx = 0
is_only = True
for idx,cnt in enumerate(cnt_box):
    for i in range(cnt):
        n_list.append(idx-4000)

    # 최빈값 탐색
    # max_idx =0 으로 초기화 했기 때문에 idx=1부터 탐색 
    if idx>0:
        if cnt > cnt_box[max_idx]:
            max_idx = idx
            is_only = True
        elif cnt == cnt_box[max_idx] and is_only:
            max_idx = idx
            is_only = False

mid = n//2
print(round(sum(n_list)/n))
print(n_list[mid])
print(max_idx-4000)
print(n_list[-1]- n_list[0])
```


# [11650번 - 좌표 정렬하기](https://www.acmicpc.net/problem/11650)
- 좌표 정렬하기 / 실버 5 / 6분
- 내부 라이브러리 이용하여 정렬
- 람다를 이용해 이중 sort 간편하게 작성
- x[0]을 우선적으로 정렬한 뒤, 같은 값에 대하여 x[1] 정렬

``` python
plane.sort(key = lambda x : (x[0],x[1]))
```

## 전체 코드

``` python
import sys
input = sys.stdin.readline
N = int(input())

plane = []
for _ in range(N):
    x,y = map(int,input().split())
    plane.append((x,y))
plane.sort(key = lambda x : (x[0],x[1]))
for x,y in plane:
    print(x,y)
``` 
