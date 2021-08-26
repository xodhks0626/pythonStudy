# 특정 원소가 속한 집합을 찾기
def find_parent(oper, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if oper[x] != x:
        return find_parent(oper, oper[x])
    return oper[x]


# 두 원소가 속한 집합을 합치기
def union_parent(oper, a, b):
    a = find_parent(oper, a)
    b = find_parent(oper, b)
    if a < b:
        oper[b] = a
    else:
        oper[a] = b


print("N번 까지의 번호를 부여하고, 입력으로 주어지는 연산의 개수 M 설정(1 <= N, M <= 100,000)")
n, m = map(int, input().split())

# 부모 테이블 초기화
oper = [0] * (n + 1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    oper[i] = i

result = []

# union 연산 수행
print("M개의 줄에 각각의 연산을 입력 (합치는 연산은 (0 a b) 형태, 같은 팀 여부 확인 연산은 (1 a b) 형태)")
for i in range(m):
    o, a, b = map(int, input().split())
    if o == 1:
        if find_parent(oper, a) != find_parent(oper, b):
            result.append(1)
        else:
            result.append(0)
    elif o == 0:
        union_parent(oper, a, b)

for i in result:
    if i == 0:
        print("YES")
    else:
        print("NO")
