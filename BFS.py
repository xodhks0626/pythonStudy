from collections import deque


def bfs(graph, start, visited):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # queue 가 빌 때 까지 반복
    while queue:
        # queue 에서 뽑아낸 원소 저장하여 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결되어 있는 것들 중
        for i in graph[v]:
            # 아직 큐에 삽입되지 않은 원소들을 삽입하고 방문처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
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

visited = [False] * 9

bfs(graph, 1, visited)
