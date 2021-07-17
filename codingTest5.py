import time

# 시간 측정
start = time.time()

# 정수 N 입력
print("N을 입력하세요 (0 <= N <= 23) : ")
N = int(input())

count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 걸린시간 출력
print("Time : ", time.time() - start)


# 처음에는
# for i in range(N+1):
#     if '3' in str(i):
#         count += 1
#     for j in range(60):
#         if '3' in str(j):
#             count += 1
#         for k in range(60):
#             if '3' in str(k):
#                 count += 1
# 이렇게 작성함.... 이렇게 하면 안되는 이유 : 03시 일때 03시 00분 00초부터 03시 59분 59초까지 모든 수가 3이 포함됨
# 따라서, count 를 계속 해서 늘려줘야하는데 그렇게 되지 않았음.
