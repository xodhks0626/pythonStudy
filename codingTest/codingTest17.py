print("N 입력 (1 <= N <= 1,000)")
N = int(input())

d = [0] * 1001

d[0] = 0
d[1] = 1
d[2] = 3

# N까지 해야하므로 3 ~ (N + 1) 구간
for i in range(3, N + 1):
    d[i] = d[i - 1] + d[i - 2] * 2

print(d[N] % 796796)
