INF = int(1e9)

# 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 주어진다.
n, m = map(int, input('N(회사의 개수)과 M(경로의 개수)에 대한 값 입력\n').split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
print("간선에 대한 정보 입력")
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# X와 K가 공백으로 구분되어 주어진다. (1 <= K <= 100)
x, k = map(int, input('X(가야할 회사)와 K(거쳐갈 회사)에 대한 값 입력\n').split())

# K번 회사를 거쳐 X번 회사로 가는 최소 이동시간 출력
# X번 회사에 도달할 수 없다면 -1 출력
# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print("2차원 배열로 나타내면")
print()
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
print()

# 결국은 graph[1][k] + graph[k][x] 을 출력하면 최단 거리가 되는 것이다.
result = graph[1][k] + graph[k][x]

if result >= INF: # INFINITY 가 둘 중 하나라도 있게 된다면 INF 보다 값이 커지게 되므로 부등호가 포함되어야 한다.
    print("-1")
else:
    print(result)
