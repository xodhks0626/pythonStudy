from collections import deque

# N, M 주어진다. (4 <= N, M <= 200)
print("직사각형의 크기(N * M)을 정하는 N, M 입력 (4 <= N, M <= 200)")
N, M = map(int, input().split())

# N개의 줄에는 각각 M개의 정수(0 또는 1)로 미로의 정보가 주어진다. 각각의 수들은 공백없이 붙어서 입력으로 제시
# 시작 칸과 마지막 칸은 항상 1
print("미로의 정보 입력 (단, 시작 칸과 마지막 칸은 항상 1로 설정)")
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
    # 마지막 칸에 0을 넣게되면, 다시 입력을 받고 싶음 => 어떻게 하면 될까?
    if arr[0][0] == 0:
        print("다시 입력")
        del arr[0]
        arr.append(list(map(int, input())))


# 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy 라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 를 이용했을 때 매우 효과적으로 해결 가능. (시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문)
# (0, 0) 지점에서부터 BFS 를 수행하여 모든 노드의 값을 거리 정보로 넣는다.
def search(x, y):
    # 이 위치에서의 상,하,좌,우 방향에 있는 정보를 얻어야 한다.
    queue = deque()
    # 현재 위치를 queue 에 삽입
    queue.append((x, y))
    # queue 가 빌 때까지 반복하게 한다.
    while queue:
        # 현재 체크할 위치를 queue 에서 빼준다.
        x, y = queue.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            # 또한, 맵 밖으로 나가는 경우가 생기지 않도록 한다. (무시하기)
            if a <= -1 or a >= N or b <= -1 or b >= M:
                continue
            # 방문해야 한다면
            if arr[a][b] == 1:
                # 방문하는 좌표 전에 있었던 값에서 1을 더한 값으로 변경 시켜주면서 이동한 거리를 세어준다.
                arr[a][b] = arr[x][y] + 1
                # 현재 좌표를 queue 에 넣어주어서 현재 위치에서 상하좌우를 탐색하도록 한다.
                queue.append((a, b))
    # 최단거리를 출력해야 하므로, 결국은 마지막에 위치한 좌표에서의 값을 출력해주면 되는 것이다.
    # 이동하면서 계속해서 이동 횟수를 측정해왔기 때문
    return arr[N-1][M-1]


print(search(0, 0))
