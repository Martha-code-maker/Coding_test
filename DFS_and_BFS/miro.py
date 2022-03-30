#첫째 줄에 두 정수 N,M이 주어집니다.
#다음 N개의 줄에는 각각 M개의 정수 (0또는 1)로 미로의 정보가 주어집니다.
#각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다.
#시작칸과 마지막 칸은 항상 1입니다.
#탐험가의 위치는 (1,1)이며 미로의 출구는(N,M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있습니다.
#괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다.
#탐험가가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
#칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0  or ny >= m:
                continue
                
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[nx][ny]+1
                queue.append((nx,ny))
    
    return miro[n-1][m-1]

miro = []
n, m = map(int, input().split())

for i in range(n):
    miro.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))

