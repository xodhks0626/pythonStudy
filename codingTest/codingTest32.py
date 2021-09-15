# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력됨
n = input()

# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력
s = ""
num = 0

for i in n:
    if i.isalpha():
        s += i
    else:
        num += int(i)

# 오름차수능로 정렬한 뒤 연결 시켜준다.
s = ''.join(sorted(s))
# 숫자 결합
s += str(num)

print(s)
