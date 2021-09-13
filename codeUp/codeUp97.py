# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1 (방향)
# 1 <= x <= 100 - h
# 1 <= y <= 100 - w
h, w = map(int, input().split())

n = int(input())

arr = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    # 가로 방향
    if d == 0:
        for j in range(l):
            arr[x - 1][y - 1] = 1
            y += 1
    else:
        for j in range(l):
            arr[x - 1][y - 1] = 1
            x += 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()
