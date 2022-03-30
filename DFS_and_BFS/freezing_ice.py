#첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다
#두번째 줇터 N+1번째 줄까지 얼음 틀의 형태가 주어집니다
#이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
#한 번에 만들 수 있는 아이스크림의 개수를 출력합니다
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)