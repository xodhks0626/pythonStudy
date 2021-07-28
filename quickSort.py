array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    # 엇갈리기 전까지
    while left <= right:
        # pivot 기준으로 pivot 보다 큰 데이터를 찾는 구간
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot 기준으로 pivot 보다 작은 데이터를 찾는 구간
        while start < right and array[pivot] <= array[right]:
            right -= 1
        # 만약, 엇갈렸다면 작은 데이터를 pivot 과 교체해줘야 함
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면, left 와 right 교체
        else:
            array[left], array[right] = array[right], array[left]
    # pivot 을 기준으로 작은 것과 큰 것을 나눠준 것
    # 이후에 왼쪽 리스트와 오른쪽 리스트에서 한번 더 quick sort 진행
    quick_sort(array, start, right - 1)
    quick_sort(array, left, end)


quick_sort(array, 0, len(array) - 1)
print(array)
