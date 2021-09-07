# 특정조건이란
# 현재 캐릭터의 점수 N 이라고 할 때
# 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미
# 예를 들어, 123,402
# N 입력 (단, 점수 N의 자릿수는 항상 짝수 형태)
n = int(input())
while len(str(n)) % 2 != 0:
    print("점수 N은 항상 짝수의 자릿수를 가지고 있어야 합니다.")
    n = int(input())

# 입력받은 정수를 문자열로 변환하여서
s = str(n)
# 절반을 나누고, 각 부분의 합을 따로 계산 한 뒤 서로 일치하는지 확인
half = len(str(n)) // 2
num1 = 0
num2 = 0

for i in range(half):
    num1 += int(s[i])

for j in range(half, len(str(n))):
    num2 += int(s[j])

if num1 == num2:
    print("LUCKY")
else:
    print("READY")
