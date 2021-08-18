from collections import deque
# Queue 구현을 위해 deque 라이브러리 사용

# stack 은 선입후출 방식이다.
# stack 예제
stack = []

# 삽입(5) -> 삽입(2) -> 삽입(3) -> 삽입(7) -> 삭제() -> 삽입(1) -> 삽입(4) -> 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최하단 원소부터 출력
print(stack)
# 최상단 원소부터 출력
print(stack[::-1])

# Queue 는 선입선출 방식이다.
# Queue 예제
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)
# 나중에 들어온 순서대로 출력하기 위해서는 역순으로 바꾼 후에 출력
queue.reverse()
print(queue)
