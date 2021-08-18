a, b = map(int, input().split())

if (bool(a) and bool(b)) or (bool(not a) and bool(not b)):
    print("True")
else:
    print("False")
