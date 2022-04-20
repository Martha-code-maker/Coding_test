n = list(map(int,input()))

sum1 = 0
sum2 = 0

for i in range(int(len(n)/2)):
    sum1 += n[i]

for i in range(int(len(n)/2),len(n)):
    sum2 += n[i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

