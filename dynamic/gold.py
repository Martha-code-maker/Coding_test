#첫째 줄에 테스트 케이스 T가 입력
#매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력,
# 둘째 줄에 n x m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력
#테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 출력
#오른쪽, 오른쪽 아래, 오른쪽 위로만 움직일 수 있음
#첫번째 열 아무 장소에서 출발 가능
#테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 출력

for tc in range(int(input())):
    n, m  = map(int, input().split())
    array = list(map(int,input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1,m):
        for i in range(n):
            if i == 0 : left_up = 0
            else: left_up = dp[i-1][j-1]
            
            if i == n-1 : left_down = 0
            else: left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = dp[i][j]+ max(left_up,left_down, left)
result = 0
for i in range(n):
    result = max(result,dp[i][m-1])
print(result)

    