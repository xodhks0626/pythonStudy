def solution(s):
    length = len(s)  # 문자열 길이 변수
    answer = length

    for j in range(1, length):
        final = ""
        first = s[0:j]
        count = 1
        for i in range(j, length, j):
            # 만약, 이어진 두 원소가 같다면
            if first == s[i:i + j]:
                count += 1
            # 이어진 두 원소가 같지 않다면
            else:
                # 현재까지 이어진 원소를 표현
                if count != 1:
                    final += str(count) + first
                    first = s[i:i + j]
                    count = 1
                else:
                    # 만약, 주어진 범위를 초과하게 되는 경우
                    if i + j >= length:
                        # 남은 원소들을 그냥 추가한다.
                        final += s[i - j:length]
                        break
                    final += first
                    first = s[i:i + j]
                    count = 1

        if count != 1:
            final += str(count) + first

        answer = min(len(final), answer)
        print(final)

    return answer


print(solution(input()))
