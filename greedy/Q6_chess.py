#행복 왕국의 왕실 정원은 체스판 같은 8x8 좌표 평면입니다.
#특정한 한 칸에 나이트가 서있습니다. 나이트는 충성스런 신하로 매일 무술을 연마합니다.
#나이트는 말을 타고 있기 때문에 이동을 할 때 L자 형태로만 이동 가능하며
#정원 밖으로 나갈 수 없다
#나이트는 특정 위치에서 다음과 같이 2가지 경우로 이동 가능하다
#1. 수평으로 두 칸이동한 뒤 수직으로 한칸 이동하기
#2. 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동하기
#나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하라.
#왕실 정원의 행 위치를 표현할 때 1-8로 표현하며, 열 위치를 표현 할 때 a-h로 표현한다.

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - ord('a') + 1
steps = [(1,-2), (3,-2), (1,2), (-1,2),(2,1),(2,-1),(-2,-1),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
        result +=1
print(result)