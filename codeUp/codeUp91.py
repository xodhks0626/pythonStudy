# 방문 주기가 공백을 두고 입력
a, b, c = map(int, input().split())

day = max(a, b, c)

i = day

while True:
    if day % a == 0 and day % b == 0 and day % c == 0:
        print(day)
        break
    else:
        day += i
