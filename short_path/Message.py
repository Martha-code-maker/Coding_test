#N개의 도시가 있다. 각 도시는 보내고자 하는 메시지가 있는 경우 다른 도시로 전보를 보내 다른 도시로 전송 가능.
#x에서 y로 보내는 경우 통로 설치 필요. 통로가 없다면 메시지 전송 불가. 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간 소요됨.
#어느날 C라는 도시에서 위급 상황 발생. 최대한 많은 도시로 메시지를 보내고자 한다. 메시지는 도시 C에서 출발하여
#각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
#각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며
#도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.
#첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input()) #노드, 간선의 수
start = int(input()) #시작 노드의 번호 입력받기
graph = [[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1)

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


n, m, start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

dijkstra(start)

count = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance,d)

print(count-1, max_distance)


