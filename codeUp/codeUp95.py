# 바둑판에 올려 놓을 흰 돌의 개수
n = int(input())

# 좌표
arr = [[0] * 19 for _ in range(19)]

# 흰 돌을 놓을 좌표 입력
for i in range(n):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ')
    print()
