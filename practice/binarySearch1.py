def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


print("원소의 개수와 찾고자하는 문자열 입력 :")
n, tar = list(map(int, input().split()))
print("전체 문자열 입력")
arr = list(map(int, input().split()))

result = binary_search(arr, tar, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)
