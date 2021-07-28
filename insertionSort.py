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
