print("두 수(N, M)를 입력하세요. N = 행,  M = 열")
N, M = map(int, input().split())
# N = 행, M = 열 의 개수

if N == 0 or M == 0:
    print("N 또는 M은 1 이상의 자연수이어야 합니다.")
    exit()

result = 0
# 결과를 출력할 변수

print("배열을 입력해주세요.")

for i in range(N):
    arr = list(map(int, input().split()))
    while len(arr) != M or arr.count(0) != 0:
        print("다시 입력해주세요.")
        arr = list(map(int, input().split()))
    # 만약, M의 개수만큼 입력하지 않았거나, 배열의 원소 중 0이 들어가게 되면 다시 입력받게 한다.
    arr.sort()
    # 오름차순으로 정렬된 배열
    result = arr[0]
    # 배열에서 가장 작은 수 선택

if result == 0:
    print("계산 실패! 결과는 ", result)
    exit()
    # 초기에 정해놓은 result 값을 출력하고 종료
else:
    print(result)
    # 올바른 결과를 출력하고 종료
