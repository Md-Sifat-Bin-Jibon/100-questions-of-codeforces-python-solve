a, b, n = map(int, input().split())

for digit in range(10):
    if (a * 10 + digit) % b == 0:
        print(str(a * 10 + digit) + "0" * (n - 1))
        break
else:
    print(-1)
