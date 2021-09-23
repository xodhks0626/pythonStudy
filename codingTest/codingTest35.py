# N * N 크기의 시험관
# 시험관은 1 * 1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재
# 바이러스의 종류는 1 ~ K 까지의 K 가지가 존재
# 시험관에 존재하는 모든 바이러스는 1초마다 상,하,좌,우의 방향으로 증식, 매초 번호가 낮은 종류의 바이러스부터 증식
# 증식과정에서 특정한 칸에 이미 어떠한 바이러스가 있다면, 그곳에서는 다른 바이러스가 못 들어간다.
# 시험관의 크기와 비이러스의 위치 정보가 주어졌을 때, S 초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램 작성
# S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력
# 시험관의 가장 왼쪽 위 = (1, 1)

# 자연수 N , K 가 주어지며 공백으로 구분
# 바꿔주는 함수
def check(a, b):
    # 상 a - 1
    if a - 1 != -1:
        if arr[a - 1][b] == 0:
            arr[a - 1][b] = arr[a][b]
    # 하 a + 1
    if a + 1 != n:
        if arr[a + 1][b] == 0:
            arr[a + 1][b] = arr[a][b]
    # 좌 b - 1
    if b - 1 != -1:
        if arr[a][b - 1] == 0:
            arr[a][b - 1] = arr[a][b]
    # 우 b + 1
    if b + 1 != n:
        if arr[a][b + 1] == 0:
            arr[a][b + 1] = arr[a][b]


# 탐색해서 0이 아닌 위치와 값을 저장해주는 것
def explore():
    loc = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                loc.append([arr[i][j], (i, j)])

    # 1, 2, 3...순서로 정렬
    loc.sort()
    return loc


n, k = map(int, input().split())

# n개의 줄에 걸쳐서 시험관의 정보가 주어진다.
# 각 행은 n개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 주어지며 공백으로 구분
# 바이러스가 존재하지 않는 곳 = 0, 모든 바이러스의 번호는 K 이하의 자연수
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# s = 초, x, y = 좌표
s, x, y = map(int, input().split())

loc = explore()

time = 1

while time != s:
    for i in range(k):
        a, b = loc[i][1]
        check(a, b)

    # 1초 동안 증식하고 난 후, 업데이트 된 시험관 상태 저장
    loc = explore()
    time += 1

print(arr[x - 1][y - 1])
