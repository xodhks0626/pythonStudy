print("N명의 모험가 (1 <= N <= 100,000)")
n = int(input())

print("N명의 모험가의 공포도 지정 (N값 이하로 지정)")
arr = list(map(int, input().split()))

# 리스트 정렬
arr.sort()

# 가장 작은 공포도부터 그룹을 배정시켜서 그룹이 최대한 많이 나오도록 한다.
count = 0
group = 0
for i in arr:
    if i == n:
        group = 1
        break

    count += 1
    if count < i:
        continue
    else:
        # 그룹을 하나 만든다. 그룹 결성 조건을 만족했으므로
        group += 1
        # 그룹의 인원을 체크하는 count 값 초기화
        count = 0

print(group)
