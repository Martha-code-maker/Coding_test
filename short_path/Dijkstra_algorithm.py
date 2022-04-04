import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input()) #노드, 간선의 수
start = int(input()) #시작 노드의 번호 입력받기
graph = [[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) #a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index += 1
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
dijkstra(start)

for i in range(1, n+1):
    if distance[1] == INF:
        print("Infitiny")
    else:
        print(distance[i])