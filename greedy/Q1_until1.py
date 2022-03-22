#N,K 를 입력받는다. 
#주어진 N이 1이 될 때까지 다음두 과정을 반복적으로 수행한다. 단, 두번째 연산은  N이 K로 나누어 떨어질 때만 선택가능
#1. N에서 1을 뺍니다
#2. N을 K로 나눕니다.
#과정을 수행해야 하는 최소 횟수를 구하는 프로그램 작성
n,k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k 
    result += (n-target)
    n = target

    if n<k:
        break
    
    result += 1
    n //= k

result += (n-1)
print(result)


