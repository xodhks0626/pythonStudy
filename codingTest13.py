import time

print("부품의 개수 N 입력 (1 <= N <= 1,000,000) : ")
N = int(input())

print("공백을 통해서 N개의 정수를 입력")
total = list(map(int, input().split()))

print("손님이 선택할 부품 종류의 수를 입력 (1 <= M <= 1,000) : ")
M = int(input())

print("공백을 통해서 M개의 정수를 입력")
arr = list(map(int, input().split()))

arr2 = []


def sequential_search(data, array):
    global arr2
    for i in range(len(array)):
        arr2.append(None)
        for j in range(len(data)):
            if array[i] == data[j]:
                del arr2[i]
                arr2.append(i + 1)
    return arr2


# 시간 측정
start = time.time()

# 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no 출력
result = sequential_search(total, arr)
for i in range(len(result)):
    if result[i] == None:
        print("no", end=' ')
        # 걸린시간 출력
        print("Time : ", time.time() - start)

    else:
        print("yes", end=' ')
        # 걸린시간 출력
        print("Time : ", time.time() - start)


