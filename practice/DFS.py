# 논리적으로 정답이 될 수 없는 큰 값 중에서 999999999, 987654321 등의 값으로 초기화
# 인접 행렬 방식
# 무한의 비용 선언
INF = 999999999

# 2차원 리스트를 이용해 인접 행렬(Adjacency Matrix) 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접 리스트 방식
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph2 = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph2[0].append((1, 7))
graph2[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
graph2[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
graph2[2].append((0, 5))

print(graph2)


# DFS 예제
def dfs(graph3, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph3[v]:
        # 만약, 방문하지 않은 노드라면 if 문 실행
        if not visited[i]:
            dfs(graph3, i, visited)


graph3 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

dfs(graph3, 1, visited)
