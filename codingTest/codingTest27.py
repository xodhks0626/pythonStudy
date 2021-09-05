# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하는 프로그램
print("동전의 개수 N 입력 (1 <= N <= 1,000)")
while True:
    n = int(input())
    if n < 1 or n > 1000:
        print("다시 입력해주세요.")
    else:
        break

# 각 동전의 화폐 단위를 나타내는 n개의 자연수를 공백으로 구분하여 입력
print("공백으로 구분하여 N개의 화폐 입력")
arr = list(map(int, input().split()))

# 오름차순으로 정렬
arr.sort()

bottom = 1
for arr in arr:
    if bottom < arr:
        break
    bottom += arr

print(bottom)

"""
다른 방법
내림 차순으로 정리한다 
-> 계산하고자 하는 화폐의 값에서 현재의 값을 뺀다
1. 만약, 음수가 나온다면 배열의 다음 값을 뺀다.
2. 만약, 양수가 나온다면 뺀 값을 새로 저장한 뒤, 배열의 다음 값을 빼준다.
3. 이를 반복한다.
-> 뺄셈을 하다가 0 이 나오게 된다면, 이는 주어진 화폐로 만들 수 있는 화폐인 것이므로 1을 더하여 다음 계산하고자 하는 화폐로 넘어간다.
-> 배열을 다 돌아도 0이 나오지 않는다면, 이는 만들 수 없는 화폐이므로 이 값을 출력

코드

arr.sort(reverse=True)
bottom = 1
exiting = 1
while True:
    target = bottom

    for i in range(len(arr)):
        if target - arr[i] != 0 and i == len(arr) - 1:
            exiting = 0
            break

        if target - arr[i] < 0:
            continue
        elif target - arr[i] >= 0:
            target = target - arr[i]

        if target == 0:
            break

    # while 문 탈출
    if exiting == 0:
        break

    bottom += 1

print(bottom)
"""
