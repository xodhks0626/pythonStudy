import time

# 시간 측정
start = time.time()

print("떡의 개수 N과 요청한 떡의 길이 M을 입력해주세요. (1 <= N <= 1,000,000 , 1 <= M <= 2,000,000,000)")
N, M = map(int, input().split())

print("떡의 개별 높이를 입력해주세요.")
data = list(map(int, input().split()))

arr = []
h = 0


def split(total, m):
    global arr, h
    arr.clear()
    for i in range(len(total)):
        j = total[i] - h
        if j >= 0:
            arr.append(j)
    if plus(arr) != m:
        h += 1
        split(total, m)
    else:
        print(h)
        return h


def plus(array):
    k = 0
    for i in range(len(array)):
        k += array[i]
    return k


split(data, M)

# 걸린시간 출력
print("Time : ", time.time() - start)
