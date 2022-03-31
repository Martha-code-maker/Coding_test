#첫째줄에 n,m이 주어진다
#이후 n개의 줄에는 각 화폐의 가치가 주어진다.
#m원을 만들기 위한 최소 화폐의 개수를 출력한다
#불가능할때는 -1을 출력

n,m = map(int,input().split())
value = []
for i in range(n):
    value.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(n):
    for j in range(value[i], m+1):
        if d[j-value[i]] != 10001:
            d[j] = min(d[j],d[j-value[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

