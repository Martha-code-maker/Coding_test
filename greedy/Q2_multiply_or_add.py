data = input()
#각 자리가 숫자 0~9로만 이루어진 문자열 S가 주어진다.
#왼쪽에서 오른쪽으로 하나씩 모든 숫자 확인하며 숫자 사이 'x' 혹은 '+'연산자를 넣어 만들 수 있는 
#가장 큰 수를 구하는 프로그램 작성하세요.
#+보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정.
result = int(data[0])

for i in range(1,len(data)):
    num = data[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)