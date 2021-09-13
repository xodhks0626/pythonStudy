arr = []

for i in range(19):
    arr.append(list(map(int, input().split())))

# 십자 뒤집기 횟수 입력, n은 10 이하의 자연수
n = int(input())

# 십자 뒤집기 좌표가 횟수만큼 입력
for i in range(n):
    x, y = map(int, input().split())
    # 뒤집기
    for j in range(19):
        # 가로줄
        if arr[x - 1][j] == 0:
            arr[x - 1][j] = 1
        else:
            arr[x - 1][j] = 0
        # 세로줄
    for k in range(19):
        if arr[k][y - 1] == 0:
            arr[k][y - 1] = 1
        else:
            arr[k][y - 1] = 0

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
