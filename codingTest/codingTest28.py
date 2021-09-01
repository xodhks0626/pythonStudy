# 두 사람이 볼링을 치고 있다.
# 서로 무게가 다른 볼링공을 고르려고 한다.
# 볼링공의 개수는 총 N개, 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여
# 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주
# 볼링공의 무게는 1부터 M 까지의 자연수 형태로 존재
# 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램 작성
print("볼링공의 개수 N, 공의 최대 무게 M을 공백으로 구분하여 입력")
n, m = map(int, input().split())

print("각 볼링공의 무게를 입력")
arr = list(map(int, input().split()))
while len(arr) != n:
    print("다시 입력해주세요.")
    arr = list(map(int, input().split()))

for i in arr:
    if i > m:
        print("다시 입력해주세요.")
        arr = list(map(int, input().split()))

count = 0

for i in range(n - 1):
    for j in range(1, n):
        if i < j:
            if arr[i] != arr[j]:
                count += 1

print(count)
