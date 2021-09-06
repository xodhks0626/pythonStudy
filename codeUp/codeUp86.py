n = int(input())
result = 0
while True:
    if n == 1:
        result = 1
        break
    for i in range(n):
        result += i
        if result >= n:
            break
    break

print(result)
