# 수열을 내림차순으로 정렬하는 프로그램

# 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
print("수열에 속해 있는 수의 개수 N을 결정하세요. (1 <= N <= 500)")
N = int(input())

array = []
# N개의 수가 입력. 수의 범위는 1 이상 100,000 이하의 자연수
for i in range(N):
    array.append(int(input()))

array.sort(reverse=True)

for i in range(len(array)):
    print(array[i], end=' ')
