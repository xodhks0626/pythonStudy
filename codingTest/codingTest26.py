# 0과 1로만 이루어진 문자열 S
# 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는다. (1을 0으로, 0을 1로 바꾸는 것을 의미)
print("0과 1로만 이루어진 문자열 S를 입력 (S의 길이는 100만보다 작다) : ")
while True:
    s = input()
    if len(s) > 1000000:
        print("다시 입력해주세요.")
    else:
        break

# 0 을 1로 바꾸는 카운트
count = 0
# 1을 0으로 바꾸는 카운트
count2 = 0

if int(s[0]) == 0:
    count += 1
else:
    count2 += 1

# 문자열을 비교해가면서 0이나 1이 이어진 길이를 파악
# 즉, 000110010이면 0을 뒤집을 경우-> 3번, 1을 뒤집을 경우-> 2번이면 되므로 둘 중 작은 횟수인 2회를 출력
for i in range(len(s) - 1):
    if int(s[i]) != int(s[i + 1]):
        if int(s[i + 1]) == 0:
            count += 1
        else:
            count2 += 1

result = min(count, count2)
print(result)
