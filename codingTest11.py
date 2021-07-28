# 학생의 수 N이 입력
print("학생의 수 N을 입력하세요. (1 <= N <= 100,000)")
N = int(input())

# 학생 정보는 학생의 이름과 학생의 성적으로 구분
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력
# 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.
array = []
for i in range(N):
    stu = input().split()
    if len(stu[0]) > 100 or int(stu[1]) > 100:
        print("학생의 이름 길이와 학생의 성적은 100 이하의 자연수입니다.")
        break
    array.append((stu[0], int(stu[1])))

result = sorted(array, key=lambda x: x[1])

for k in result:
    print(k[0], end=' ')
