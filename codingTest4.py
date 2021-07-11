import time

# 시간 측정
start = time.time()

# N * N 크기의 공간
N = int(input("N : "))
# 계획서가 존재 -> 문자열을 split 을 통해 분할하여 받는다.
M = input("계획서 입력 : ").split()

# 처음 지점은 (1,1)로 고정
a = 1
b = 1

# 문자열 비교해서 이동시키기 (받은 문자열의 길이 만큼 반복하게 된다.)
for i in range(len(M)):
    # a가 1에서 N범위 내에서 움직여야하므로
    if 1 <= a <= N:
        # a가 1일 경우 U을 수행할 수 없음
        if a != 1 and M[i] == 'U':
            a -= 1
        # a가 N일 경우 D를 수행할 수 없음
        elif a != N and M[i] == 'D':
            a += 1
    # 마찬가지로 b도 범위 내에서 움직여야하므로
    if 1 <= b <= N:
        # b가 N일 경우 R을 수행할 수 없음
        if b != N and M[i] == 'R':
            b += 1
        # b가 1일 경우 L을 수행할 수 없음
        elif b != 1 and M[i] == 'L':
            b -= 1

# 마지막으로 도착 좌표 출력
print(a, b)

# 걸린시간 출력
print("Time : ", time.time() - start)
