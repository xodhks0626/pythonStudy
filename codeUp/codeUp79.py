a = int(input())
i = 0
result = 0
while True:
    i += 1
    result += i
    if result >= a:
        print(i)
        break
