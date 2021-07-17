# Recursive Function (재귀 함수) : 자기 자신을 다시 호출하는 함수
def recursive_function():
    print("재귀함수")
    recursive_function()


recursive_function()
# 마지막에 나타나는 오류 메시지는 재귀의 최대 깊이를 초과했다는 내용이다.  => 무한대로 재귀 호출을 할 수 없다.
