# N가지 종류의 화폐, 화폐들의 개수를 최소한으로 사용하여 합이 M이 되도록한다.
# 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분
print("N가지 종류의 화폐(1 <= N <= 100)와 합 M을 입력(1 <= M <= 10,000)")
N, M = map(int, input().split())

print("N개의 줄에 각 화폐의 가치를 입력 (10,000보다 작거나 자연수)")
arr = []
for i in range(N):
    arr.append(int(input()))

d = [10001] * (M + 1)

d[0] = 0

for i in range(N):
    # 한 화폐를 가지고, 계산 가능한 경우들의 값들을 변경
    for j in range(arr[i], M + 1):
        # 계산 가능한 경우에는 0이 아니라 다른 값이 저장. 이때 min 을 통해서 바꿀 수 있더라도 최소값을 저장하도록 한다.
        d[j] = min(d[j], d[j - arr[i]] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
