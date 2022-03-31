#첫째 줄에 n이 주어진다
#둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어진다
#첫째 줄에 남아있는 병사의 수가 최대가 되도록 하기 위해 열외시켜야 하는 병사의 수를 출력한다

n = int(input())

array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if array[j] <array[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))