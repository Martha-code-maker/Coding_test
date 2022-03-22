#알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어집니다.
#이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든
#숫자를 더한 값을 이어서 출력합니다.
#첫째 줄에 하나의 문자열 S가 주어집니다.

from sympy import S


s = input()
letter = []
sum = 0

for x in s:
    if x.isalpha():
        letter.append(x)
    else:
        sum += int(x)

letter.sort()
if sum != 0:
    letter.append(str(sum))

print(''.join(letter))


