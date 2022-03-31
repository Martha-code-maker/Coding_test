#첫째 줄에 떡의 개수 N과 손님이 요청할 떡의 길이 M을 입력한다
#둘째 줄에는 떡의 개별 높이를 입력한다. 떡 높이의 총합은 항상 M이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
#높이는 10억보다 작거나 같은 양의 정수 또는 0이다
#적어도 M만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다

n, m  = list(map(int,input().split()))
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end)/2
    for x in array:
        #잘랐을 때 떡의 양 계산
        if x > mid:
            total += x-mid
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid
        start = mid + 1
print(result)