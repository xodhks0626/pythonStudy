from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
n, m, k, x = map(int, input().split())

# M개의 줄에 걸쳐서 두개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)


length = [0] * (n + 1)

queue = deque([x])
while queue:
    v = queue.popleft()
    for i in arr[v]:
        if length[i] == 0:
            length[i] = length[v] + 1
            queue.append(i)

num = 0

for i in range(1, n + 1):
    if length[i] == k:
        print(i)
        num += 1

if num == 0:
    print(-1)
