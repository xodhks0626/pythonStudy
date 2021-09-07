def solution(food_times, k):
    answer = 0
    for i in range(k + 1):  # 1초 ~ K초
        j = i
        if j == k:  # 통신 장애가 발생한 시간
            j %= len(food_times)  # K초 까지 먹은 음식 번호
            if food_times[j] != 0:
                answer = j
            else:
                while food_times[j] == 0:
                    j += 1
                    j %= len(food_times)
                answer = j

        # i = 3, 4, 5... 인 경우
        if j >= len(food_times):
            # 0, 1, 2 로 바꿔줌
            j %= len(food_times)
            # 만약, 현재 위치에 먹을 음식이 없다면 먹을 위치까지 옮긴다.
            while food_times[j] == 0:
                j += 1
                j %= len(food_times)
            # 정해진 음식을 먹는다.
            food_times[j] -= 1

        else:  # i = 0, 1, 2 일 때의 음식 섭취
            if food_times[j] != 0:  # 먹을 음식이 있는 경우에만 돌아간다.
                # 정해진 음식을 먹는다.
                food_times[j] -= 1
            else:  # 원래 먹을 위치의 음식이 없는 경우
                # 다음에 먹을 음식들을 조사하여, 음식이 있는 경우를 택하게 한다.
                while food_times[j] == 0:
                    j += 1
                    j %= len(food_times)
                # 다음 먹을 음식이 다 선택되고 나면 음식 섭취
                food_times[j] -= 1

        # answer 는 0, 1, 2로 저장되므로 몇 번째 음식을 나타내기 위해서는 1을 더해준다.
        answer += 1
        # for 문 끝
    return answer


print(solution([1000, 1000, 1000], 1))
