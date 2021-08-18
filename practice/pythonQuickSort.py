array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    # pivot 은 첫번째 원소
    pivot = array[0]
    # pivot 을 제외한 나머지 리스트
    tail = array[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x > pivot]

    # 분할 하고 나서, 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 한번 더 수행시킨다.
    # 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
