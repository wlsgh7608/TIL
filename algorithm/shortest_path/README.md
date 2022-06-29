# 최단경로 알고리즘(Shortest Path)
## 가장 짧은 경로를 찾는 알고리즘
- 한 지점에서 다른 특정 지점까지의 최단 경로
- 모든 지점에서 다른 모든 지점까지의 최단 경로

## 사용 알고리즘
- 다익스트라(Dijkstra)
- 벨만 포드(Bellman-Ford)
- 플로이드 워셜(Floyd-Warshall)

## 다익스트라(Dijkstra) 최단 경로 알고리즘
- 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- __음의 가중치__ 이 없을 때 정상적으로 동작
- GPS 소프트웨어의 기본 알고리즘

### 작동 원리
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3~4 반복


<img src ="https://www.google.com/url?sa=i&url=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3ADijkstra_Animation.gif&psig=AOvVaw1h2zNwT7mV4NfPI7Bv9Tk7&ust=1649674004448000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCNDO5NyoifcCFQAAAAAdAAAAABAO">
출처 - https://commons.wikimedia.org/wiki/File:Dijkstra_Animation.gif
