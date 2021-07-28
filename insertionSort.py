array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # i부터 1까지 감소하며 반복하는 문법
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            # 3의 경우처럼 자기보다 작은 데이터를 만나면 그 위치에서 멈추게 함
            break

print(array)

# range 의 매개 변수는 3개 (start, end, step) 이다.
# 세 번째 매개 변수인 step 에 -1이 들어가면 start 인덱스부터 시작해서 end + 1 인덱스까지 1씩 감소
