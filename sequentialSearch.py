def sequential_search(n, tar, array):
    for i in range(n):
        if tar == array[i]:
            return i + 1


print("생성할 원소 개수(N)와 찾을 문자열을 입력하세요.")
data = input().split()
N = int(data[0])
target = data[1]

print("N 개수 만큼의 문자열을 입력하세요.")
arr = input().split()
if len(arr) != N:
    print("N 개수 = ", N, "입니다.")

print("찾고자하는 문자열(", target, ")은 배열의", sequential_search(N, target, arr), "번째에 존재합니다.")
