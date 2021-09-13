# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.
# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.
# 미로 상자의 테두리는 모두 벽으로 되어 있으며, 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.
arr = []

for i in range(10):
    arr.append(list(map(int, input().split())))

arr[1][1] = 9
i = 1
j = 2

while True:
    if arr[i][j] == 0:
        arr[i][j] = 9
        if i == 8 and j == 8:
            break
        j += 1
    elif arr[i][j] == 1:
        i += 1
        j -= 1
    elif arr[i][j] == 2:
        arr[i][j] = 9
        break
    elif i == 9 and j == 9:
        break

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()
