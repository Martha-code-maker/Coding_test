s = input()
data = []

summary = 0
for i in s:
    if i.isalpha():
        data.append(i)

    else:
        summary += int(i)

data.sort()

if summary != 0:
    data.append(str(summary))

print(''.join(data))





