# 출석 번호를 부른 횟수 n
n = int(input())

# 무작위로 부른 n 개의 번호 리스트
k = input().split()

for i in range(n - 1, -1, -1):
    print(k[i], end=' ')
