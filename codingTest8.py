import time

# 시간 측정
start = time.time()

# N * M 크기의 얼음 틀 설정
print("N, M을 입력해주세요. (1 <= N, M <= 1,000) : ")
N, M = map(int, input().split())

# 얼음 틀의 형태 입력
print("얼음 틀에 대한 정보 입력 (0 : 구멍이 뚫려있는 부분, 1 : 그렇지 않은 부분)")
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

# 묶음을 지어줄 배열 선언.
spot = []
# 한 번에 만들 수 있는 아이스크림의 개수 구하기
# 정해진 지점에서 상,하,좌,우를 살펴본 뒤 주변 지점 중에서 값이 0이면서, 아직 방문하지 않은 지점이 있다면 그 지점 방문
# 한 지점을 선택하고 이동하면서 확인을 하게 되면, 반대쪽으로 다시 못 돌아온다 => 이 부분은 재귀함수로 해결할 수 있을 것.
# 위로 갔으면 거기서 상,하,좌,우 탐색하는 함수 실행, 아래로 갔으면 거기서도 함수 실행 ...
# 부분들을 묶어주는 것이 필요 => 더이상 연결되지 않는 부분들이 무조건 존재할 것임 => 그 전까지 0인 부분들을 모은 배열을 만들어준다.


def search(x, y):
    global arr, spot
    # 범위를 벗어나지 않도록 하는 것이 필요. => 그냥 종료시킨다.
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return -1
    if arr[x][y] == 0:
        # 방문 처리
        arr[x][y] = 1
        # 또 다른 배열에 이 부분을 추가
        spot.append([x, y])
        # 이 위치에서의 주변의 것들도 재귀 함수로 실행
        # 상
        search(x-1, y)
        # 하
        search(x+1, y)
        # 좌
        search(x, y-1)
        # 우
        search(x, y+1)


# 묶음이 끝난 후, 그 개수를 세기위한 변수
count = 0

# 만약, dfs(한 위치) 로만 실행하게되면 한 부분만 찾을 수 있음 => 이를 해결하기 위해서 전체 배열을 한 번씩 도는 for 문이 필요
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            search(i, j)
            count += 1
            # 배열 다시 초기화 => 새로운 묶음을 지어주기 위해서
            spot = []

print("총 아이스크림 개수 : ", count)

# 걸린시간 출력
print("Time : ", time.time() - start)
