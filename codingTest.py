print("N, M, K의 값을 순서대로 작성해주세요. (N = 배열의 길이, M = 더해지는 횟수, K = 연속가능한 횟수)")
N, M, K = map(int, input().split())
if N == 0 or M == 0 or K == 0:
    print("값을 0으로 설정하셨습니다. 1이상의 값으로 설정바랍니다.")
    exit()
# map은 리스트의 요소를 지정된 함수(int)로 처리해주는 함수이다.
# 현재 map을 통해서 3가지의 정수를 공백으로 구분하여 줌으로써 연속해서 입력을 받고 이를 int형의 함수형으로 처리
# 이제 N값을 가지고 배열을 하나 만들어야한다.
arr = list(map(int, input().split()))
if len(arr) != N:
    print("정수의 개수가 N 값과 일치하지 않습니다.")
    exit()
# 만약 배열에 들어갈 수를 입력하는데 N의 값에 맞지 않게 입력하게 된다면 종료하게 만들어준다.
# map을 통해서 int형으로 처리해주고 그 결과를 list를 통해 배열로 만들어 줌.
# 입력받은 정수 배열에서 가장 큰 두 수를 찾아서 제일 큰 수를 2번 더하고, 두번째로 큰 수를 1번 더한다.
arr.sort(reverse=True)
# 가장 큰 두 수를 찾기 위해서 배열을 내림차순으로 정렬해준다.
# 이제 첫번 째 수가 제일 큰 수가 된 것이다. 이를 따로 저장해준다.
big1 = arr[0]
big2 = arr[1]
# 배열의 첫번째와 두번째 수를 따로 저장함.
# 이제 해야할 것이 M과 K의 값에 따라서 얼마나 더해야하는지 결정
count = 0
result = 0
# count는 M의 값과 같은지 판단하기 위한 변수, result는 더해지는 값을 저장하는 변수이다.
while True:
    for i in range(K):
        if count == M:
            break
        result += big1
        count += 1
    result += big2
    count += 1
    if count == M:
        break
# while문 안에서 가장 큰 값을 K번 반복하면서 result에 값을 더해주며 저장해주고, K번 더했으면 두번째로 큰 수를 저장해준다.
# 만약 한 싸이클안에 count와 M이 서로 다르면 다시한 번 for문을 통해 가장 큰 값을 더해주며, count가 M과 일치하면 while문을 빠져나온다.
print(result)
