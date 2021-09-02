def solution(food_times, k):
    answer = 0
    for i in range(k + 1):
        if i == k:
            i %= len(food_times)
            if food_times[i] != 0:
                answer = i
            else:
                while food_times[i] == 0:
                    i += 1
                    if i == len(food_times):
                        i -= len(food_times)
                answer = i

        if i >= len(food_times):
            i %= len(food_times)
            while food_times[i] == 0:
                i += 1
                if i == len(food_times):
                    i -= len(food_times)
            # 정해진 음식을 먹는다.
            food_times[i] -= 1
        else:
            while food_times[i] == 0:
                i += 1
                if i == len(food_times):
                    i -= len(food_times)
            # 정해진 음식을 먹는다.
            food_times[i] -= 1

        # answer 는 0, 1, 2로 저장되므로 몇 번째 음식을 나타내기 위해서는 1을 더해준다.
        answer += 1
    return answer


# 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 food_times
# 네트워크 장애가 발생한 시간 K초
# 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성
# 만약, 더 섭취해야 할 음식이 없다면 -1 반환

# 정확성 테스트 제한 사항
# food_times 의 길이는 1이상 2000 이하
# food_times 의 원소는 1이상 1000 이하의 자연수
# K는 1이상 2,000,000 이하의 자연수

# 효율성 테스트 제한 사항
# food_times 의 길이는 1이상 200,000 이하
# food_times 의 원소는 1이상 100,000,000 이하의 자연수
# K는 1이상 2 * 10^13 이하의 자연수

# 입출력 예시
# food_times = [3, 1, 2],  k = 5, result = 1

print(solution([3, 1, 2], 5))
