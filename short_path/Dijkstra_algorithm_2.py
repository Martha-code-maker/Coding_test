import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input()) #노드, 간선의 수
start = int(input()) #시작 노드의 번호 입력받기
graph = [[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) #a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[1])