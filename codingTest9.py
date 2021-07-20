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


# BFS 를 이용했을 때 매우 효과적으로 해결 가능. (시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문)
# (1, 1) 지점에서부터 BFS 를 수행하여 모든 노드의 값을 거리 정보로 넣는다.
def search(x, y):
    queue = deque()
    # queue 에 삽입
    queue.append((x, y))
    # 이 위치에서의 상,하,좌,우 방향에 있는 정보를 얻어야 한다.
    # 하 또는 우 방향으로 이동가능하면 둘 중 한 곳을 선택하게 한다.


search(0, 0)
