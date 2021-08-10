import time

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
    if plus(arr) > m:
        h += 1
        split(total, m)
    else:
        h -= 1
        print(h)
        return h


def plus(array):
    k = 0
    for i in range(len(array)):
        k += array[i]
    return k


# 시간 측정
start = time.time()

split(data, M)

# 걸린시간 출력
print("Time : ", time.time() - start)


"""
모범 답안
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        만약, 떡의 개별 높이가 중간점보다 클 경우
        if x > mid:
            total += x - mid
    떡의 양이 부족한 경우 더 많이 자르기 위해서 끝점을 옮긴다(왼쪽 부분 탐색)
    if total < m:
        end = mid -1
    else:
        최대한 덜 잘랐을 때가 정답이므로, result 에 기록
        result = mid
        start = mid + 1

print(result)
"""
