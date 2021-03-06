import time

# 시간 측정
start = time.time()

# 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력
# 3 <= N, M <= 50
print("N, M을 입력해주세요. (3 <= N, M <= 50) : ")
N, M = map(int, input().split())

# 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
# A = 북쪽으로부터 떨어진 칸의 개수, B = 서쪽으로부터 떨어진 칸의 개수
# 방향 d의 값으로는 4가지가 존재 (0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽)
print("캐릭터가 있는 칸의 좌표 (A, B) 와 바라보는 방향 d를 입력해주세요. (방향 => 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽)")
A, B, d = map(int, input().split())

# 맵이 육지인지 바다인지에 대한 정보입력, 외곽은 항상 바다 (0 : 육지, 1 : 바다)
# N 개의 줄에 북 -> 남, 서 -> 동 순서대로 주어진다.
print("육지인지 바다인지에 대한 정보입력 (0 : 육지, 1 : 바다)")
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy 라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
# 예를 들면, dx[0] 와 dy[0] => 북쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# result = 방문한 결과, count = 회전한 횟수
result = 0
count = 0

# 방문한 위치를 표시해주는 것이 필요 => 0 으로 표시된 육지를 1 로 표시하게 만든다?
# 이동하고 나면 현재위치 (A, B)의 0 -> 1로 표시
# 맵을 그대로 복사한 location 을 만들고, 이를 조작한다.
location = arr


def visited(x, y):
    global location, result
    if location[x][y] != 1:
        location[x][y] = 1
        result += 1


# 반시계 방향으로 90도 회전 시키고, 왼쪽 방향에 방문하지 않았다고 하면 한번 더 회전한다음 왼쪽으로 한 칸 이동
# 회전하는 함수
def turn():
    # global 은 함수 바깥에서 선언된 전역변수를 사용하므로 나타낸 표현
    global d
    d -= 1
    # 만약 -1이 되면, 이는 서쪽을 나타내어야 하므로 3을 나타내기 위해 if문 을 사용함
    if d == -1:
        d = 3
        print("바라보는 방향 = 서쪽")
    elif d == 0:
        print("바라보는 방향 = 북쪽")
    elif d == 1:
        print("바라보는 방향 = 동쪽")
    else:
        print("바라보는 방향 : 남쪽")
# 방문하지 않은 칸이 없다면, 회전만 한다.
# 이를 수행하는 코드가 필요


while 1:
    # 시작 위치를 바로 방문처리 해준다.
    visited(A, B)
    turn()
    count += 1
    # 회전한 방향쪽으로 이동하고 난 후의 좌표 저장
    a = A + dx[d]
    b = B + dy[d]
    print("이동할 장소 정보 : (", a, ",", b, ")", "location = ", location[a][b])
    # 만약, 회전한 방향의 정면이 가보지 않은 곳이라면, 방문처리하고 그곳으로 이동 (현재 좌표를 옮긴다.)
    if location[a][b] != 1:
        print("이동! (", A, ",", B, ") -> (", a, ",", b, ")")
        visited(a, b)
        A = a
        B = b
        count = 0
    # 회전한 방향의 정면이 가본 곳이거나 바다라면, 한번 더 회전하고 4번 회전을 하고 나면 바라보는 방향 유지한 채 한칸 뒤로간다.
    elif count == 4:
        # 뒤로 한 칸 가기위해서 빼어주게 된다.
        a = A - dx[d]
        b = B - dy[d]
        # 1단계로 돌아가기 위해 count = 0 으로 재설정.
        count = 0
        # 만약, 이동할 칸이 1로 되어있으면 더 이상 이동 불가능하므로 종료
        if location[a][b] == 1:
            break


print("종료 결과 : ", result)

# 걸린시간 출력
print("Time : ", time.time() - start)
