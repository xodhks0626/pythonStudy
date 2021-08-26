from collections import deque
import copy

# 강의의 수 N 입력
print("강의의 수 N 입력 (1 <= N <= 500)")
n = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)

# 각 노드에 연결된 간선 정보를 담기위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(n + 1)]

# 강의 시간 초기화
time = [0] * (n + 1)

# 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분
print("강의 시간, 선수강의를 입력하고 난 후, -1을 입력하여 마침을 나타내는 표현을 입력")
for i in range(1, n + 1):
    # list 를 통해서 선수강의가 없는 경우를 만들 수 있다.
    m = list(map(int, input().split()))
    time[i] = m[0]
    # 선수강의가 많을 경우가 있으므로 리스트에서 시간을 제외한 부분부터 -1이 입력된 부분까지를 체크
    for j in m[1:-1]:
        indegree[i] += 1
        graph[j].append(i)


# 위상 정렬 함수
def topology_sort():
    # 리스트의 값을 복제해야 할 때는 deepcopy() 함수를 사용한다.
    # 단순히 대입 연산을 하면 값이 변경 될 때 문제가 발생할 수 있기 때문이다.
    # 이를 사용하지 않고 result = [0] * (n + 1) 로 했었다.
    # 이렇게 하게 된다면 초기값이 0으로 설정되어 있기 때문에 첫번째 값은 0이 나오고 다른 것들도 비교가 제대로 되지 않는다.
    result = copy.deepcopy(time)
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1을 빼기
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()
