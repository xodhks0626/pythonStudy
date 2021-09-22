# key 는 M * M(3 <= M <= 20, M은 자연수) 크기의 2차원 배열
# lock 은 N * N(3 <= N <= 20, N은 자연수) 크기의 2차원 배열
# M은 항상 N 이하
# key 와 lock 의 원소는 0 또는 1로 이루어져 있다.
# 0은 홈 부분, 1은 돌기 부분

# N, M 입력받기
print("N, M을 공백으로 구분하여 입력")
n, m = map(int, input().split())

arr1 = []
arr2 = []

print("M * M 크기의 내용 입력")
for _ in range(m):
    arr1.append(list(map(int, input().split())))

print("N * N 크기의 내용 입력")
for _ in range(n):
    arr2.append(list(map(int, input().split())))


def solution(key, lock):
    answer = True
    global m
    # 시계 방향 270도 회전
    for i in range(m):
        key = [k[::-1] for k in zip(*key)]

    return answer


print(solution(arr1, arr2))
