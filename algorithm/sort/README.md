# 정렬이란?

데이터를 특정한 기준에 따라서 순서대로 나열하는 것
정렬을 통하여 이진탐색(Binary Search) 가능
정렬 알고리즘 종류 : 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬


## 선택정렬
가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번 째 데이터와 바꾸는 과정

<img width ='500' src = "https://user-images.githubusercontent.com/62232531/158822529-3d216651-89e0-4c8e-a0eb-b41e25338647.gif">

선택정렬 코드
``` python
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_idx = i
    if arr[min_idx] > arr[i]:
        min_idx= i
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
```

시간복잡도 - O(n^2)

## 삽입 정렬
데이터를 하나씩 확인하여, 각 데이터를 적절한 위치에 삽입하는 정렬
필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬된 형태'일 때 효율적

<img width ='500' src="https://user-images.githubusercontent.com/62232531/158822556-1b5a8300-2663-447f-b17b-bc70fca6eb73.gif">

``` python
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
        else:
            break
print(arr)
```
시간복잡도 - O(n^2)
최선의 경우 - O(n)

## 퀵 정렬
기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬 알고리즘
평균 시간 복잡도 - O(NlogN)
최악의 경우 시간 복잠도 - O(N^2)
          
<img width='500' src ="https://user-images.githubusercontent.com/62232531/158823413-9d958547-83a0-40d0-911b-b4c135b7f956.gif">

## 계수 정렬(Count Sort)
- 특정한 조건이 부합할 때(데이터의 범위가 적음) 매우 빠른 정렬 알고리즘
  - 평균 시간 복잠도 - O(N+K)
- 정렬 알고리즘 중에서 기수 정렬(Radix Sort)와 더불어 가장 빠른 알고리즘
          
<img width ='500' src ="https://user-images.githubusercontent.com/62232531/158822737-3e4d7126-6140-4e67-8767-76bae6e3743f.gif">

### Count Sort의 공간 복잡도
- 데이터의 범위 만큼의 공간을 차지 -> 데이터의 범위가 적을 경우 비효율적
- O(N+K)

``` python
arr = [7,5,9,0,3,1,6,2,4,8]
count = [0] * (max(arr)+1) # 0으로 초기화

for i in range(len(arr)):
    count[arr[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')

```

## 파이썬의 정렬 라이브러리
- 기본 라이브러리인 sorted() 함수
- 퀵 정렬과 동작 방식이 비슷한 병합정렬 기반으로 만들어짐
- 최악의 경우에도 시간복잡도 O(NlogN) 보장
- 리스트 반환

``` python
arr = [7,5,9,0,3,1,6,2,4,8]
result = sorted(arr)
print(result)

```

### 리스트 객체의 내장 함수 sort()
- 리스트의 내부 원소가 직접 정렬

``` python
arr = [7,5,9,0,3,1,6,2,4,8]
arr.sort()
print(arr)
```
### 내부 정렬 라이브러리에서는 key 매개변수를 입력으로 받을 수 있음
- 하나의 함수가 들어가야 함 
- key 값 : 정렬 기준


### 데이터의 두 번째 원소를 기준으로 정렬

``` python
arr = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(arr,key= setting)

```

# 정렬 알고리즘 3가지 유형
1. 정렬 라이브러리로 풀 수 있는 문제 : 기본 정렬 라이브러리 사용 방법 숙지
2. 정렬 알고리즘의 원리에 대해 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 함
3. 더 빠른 정렬이 필요한 문제 : Count Sort등의 다른 정렬 알고리즘을 이용하거나 기존의 알고리즘을 구조적인 개선을 거쳐야 함
