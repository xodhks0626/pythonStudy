# 어딘가를 거쳐가는 문제가 아니라 최단 거리만 묻는 문제이므로 다익스트라 문제라고 생각 가능
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
# (1 <= N <= 30,000 , 1 <= M <= 200,000 , 1 <= C <= N)
n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]
time = [INF] * (n + 1)

# (m + 1)번 반복문을 통해 통로에 대한 정보 X, Y, Z가 주어진다.
# 특정 도시 X에서 다시 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미
# (1 <= X , Y <= N , 1 <= Z <= 1,000)
for i in range(1, m + 1):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0
    # q가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        t, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if time[now] < t:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = t + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 함수를 실행하게되면, C에서 다른 도시까지 이동할 수 있는 최단 시간이 저장된다.
# 최단 시간이 아닌 경우, INF 값이 들어가있음.
# INF 가 아닌 경우만 찾으면 메시지를 받을 수 있는 도시의 총 개수를 찾을 수 있다.
# 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력
dijkstra(c)

count = 0
result = 0
for i in time:
    if i != INF and i != 0:
        count += 1
        if result < i:
            result = i

print(count, result)
"""
count, result = 0
for i in range(1, m + 1):
    x, y, z = map(int, input().split())
    if x == c:
        count += 1
        if result < z:
            result = z

print(count, result)
"""