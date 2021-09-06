w, h, b = map(int, input().split())

n = w * h * b / 8 / 1024 / 1024

# 처음에 round 함수를 썼는데 틀렸다.
# round 함수는 불필요한 0은 없애기 때문에, print('%.2f'%n) 서식문자를 이용해 풀어야한다.
print('%.2f' % float(n), "MB")
