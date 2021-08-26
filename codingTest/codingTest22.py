# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


print("집의 개수 N, 길의 개수 M 입력 (2 <= N <= 100,000 , 1 <= M <= 1,000,000)")
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = []

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

print("a번 집과 b번 집을 연결하는 길의 유지비 c 를 차례대로 입력하세요. (1 <= c <= 1,000)")
for _ in range(m):
    a, b, c = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((c, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(c)

# 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거
result.sort(reverse=True)
del result[0]

ans = 0

for i in result:
    ans += i

# 길을 없애고 남은 유지비 합의 최솟값 출력
print(ans)
