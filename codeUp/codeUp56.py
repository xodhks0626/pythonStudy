a, b = map(int, input().split())

if (bool(a) and bool(not b)) or (bool(not a) and bool(b)):
    print("True")
else:
    print("False")
