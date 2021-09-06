# 30보다 작은 정수가 입력
n = int(input())

for i in range(1, n + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')
