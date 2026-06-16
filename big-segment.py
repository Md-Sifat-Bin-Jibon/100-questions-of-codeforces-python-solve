n = int(input())

segments = []
min_left = float('inf')
max_right = -1

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

    min_left = min(min_left, l)
    max_right = max(max_right, r)

for i in range(n):
    l, r = segments[i]

    if l == min_left and r == max_right:
        print(i + 1)  # 1-based indexing
        break
else:
    print(-1)