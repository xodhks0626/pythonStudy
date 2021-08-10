d = [0] * 100


def fibo(x):
    print("here", x)
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        print("x", x)
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    print("d[",x,"] =", d[x])
    return d[x]


print(fibo(6))


# 왜 here 2 가 나오는 것인가?
# return d[x] 를 했으면 d[3] = 2 에서 x = 2 값으로 넣어준 것인가?
# 순서가 어떻게 되는 것인지 잘 모르겠다.
