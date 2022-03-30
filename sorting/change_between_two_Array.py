#첫째 줄에 N,K가 공백을 기준으로 구분되어 입력
#두 번째 줄에 배열 A의 원소들이 공백을 기준으로 입력된다.
#세번째 줄에 배열 B의 원소들이 공백을 기준으로 구분되어 입력된다.
#N은 원소의 개수, K는 원소끼리 바꿔치기 연산을 수행하는 횟수
#총K번 바꿔치기 연산 수행 후 배열 A의 모든 원소의 합의 최댓값 출력하기

n, k = map(int, input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i],a[i]
    
    else:
        break
print(sum(a))