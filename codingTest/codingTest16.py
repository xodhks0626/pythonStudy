import time

# 식량창고의 개수 N이 주어진다
print("식량창고의 개수 N 지정 (3 <= N <= 100) :")
N = int(input())

print("공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K 지정 (0 <= K <= 1,000) :")
K = list(map(int, input().split()))

# 시간 측정
start = time.time()

d = [0] * 100

d[0] = K[0]
# 1번째와 2번째 중 큰 수를 저장
d[1] = max(K[1], K[0])
# 전체를 돌면서 현재와 2칸 앞의 수량의 합과 그 사이의 값과 비교하여 큰 값을 저장
# 계속 진행하면서 앞의 수량의 합을 저장해놓게 되므로 진행해도 무관하다.
for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + K[i])

# 결국, 마지막 칸에 들어있는 수를 출력하면 된다.
print(d[N - 1])

# 시간 측정
start = time.time()

# 걸린시간 출력
print("Time : ", time.time() - start)
