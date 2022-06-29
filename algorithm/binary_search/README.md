# 이진 탐색

## 순차 탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

``` python
def sequential_search(n,target,arr):
    for i in range(n):
        if arr[i] == target:
            return i +1
        

print('생성할 원소 개수를 입력한 뒤 찾을 문자열 입력')
n, target = input().split()
n = int(n)

print("문자열 입력")
arr = input().split()

print(sequential_search(n,target,arr))

```

최악의 경우 시간 복잡도 - O(N)

## 이진 탐색 : 바능로 쪼개면서 탐색
배열 내부의 데이터가 정렬되어 있을 때만 사용 가능한 알고리즘
사용하는 변수 : 시작점, 끝점, 중간점
찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 데이터를 찾음

최악의 경우 시간 복잡도 - O(logN)


### 구현하는 방법
1. 재귀 함수
``` python
def binary_search(array,target,start,end):
    if start > end :
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,end-1)
    else:
        return binary_search(array,target,mid+1,end)

n, target = map(int,input().split())
arr = list(map(int,input().split()))
result = binary_search(arr,target,0,n-1)
if result == None:
    print("존재 X")
else:
    print(result+1)
```

2. 반복문

``` python
def binary_search(array,target,start,end):
    while start<=end:

        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1 
        else:
            start = mid +1
    return None
n, target = map(int,input().split())
arr = list(map(int,input().split()))
result = binary_search(arr,target,0,n-1)
if result == None:
    print("존재 X")
else:
    print(result+1)
```

## 트리 자료구조
- 데이터베이스는 내부적으로 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있음
- 이진 탐색과 유사한 방법을 이용해 탐색을 항상 빠르게 수행하도록 설계

<img src = 'https://miro.medium.com/max/975/1*PWJiwTxRdQy8A_Y0hAv5Eg.png'>
출처 : <a href = 'https://towardsdatascience.com/8-useful-tree-data-structures-worth-knowing-8532c7231e8c'>'https://towardsdatascience.com/8-useful-tree-data-structures-worth-knowing-8532c7231e8c'


 - 트리는 부모 노드와 자식 노드의 관계로 표현
 - 트리의 최상단 노드를 루트 노드라고 부름
 - 트리의 최하단 노드를 리프 노드라고 부름
 - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 부름
 - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기 적합

 ## 이진 탐색 트리


 <img src = "https://blog.penjee.com/wp-content/uploads/2015/11/binary-search-tree-sorted-array-animation.gif">

 출처 : <a href = "https://blog.penjee.com/5-gifs-to-understand-binary-search-tree/">https://blog.penjee.com/5-gifs-to-understand-binary-search-tree

## 이진 트리 특징
- 부모 노드보다 왼쪽 자식 노드가 작다
- 부모 노드보다 오른쪽 자식 노드가 크다

왼쪽 자식 노드 < 부모 노드 < 오른쪾 자식 노드


## 빠르게 입력 받기

데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속독 ㅏ느리므로
sys 라이브러리의 readline()함 수 이용

``` python
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
```