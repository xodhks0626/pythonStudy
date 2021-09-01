print("여러 개의 숫자로 구성된 하나의 문자열 S 입력 (1 <= S의 길이 <= 20) :")
while True:
    s = input()
    if len(s) < 1 or len(s) > 20:
        print("다시 입력하세요.")
    else:
        break

# 문자열의 첫번째와 두번째를 통해서 +, * 연산을 하고 그 값을 다른 변수에 저장
# 그 변수들을 비교해서 큰 값이 나오게하는 연산을 선택할 수 있다.
first = int(s[0])

for i in range(1, len(s)):
    second = int(s[i])
    if first + second <= first * second:
        first = first * second
    else:
        first = first + second

print(first)
