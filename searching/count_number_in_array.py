#첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력
#둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력
#수열의 원소 중에서 값이 x인 원소의 개수 출력
#단 x인 원소가 하나도 없다면 -1출력
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index-left_index

n, x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_range(array, x,x)
if count == 0:
    print(-1)
else:
    print(count)


