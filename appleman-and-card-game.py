from collections import Counter

n, k = map(int, input().split())
s = input()

frequency = Counter(s)

frequencies = sorted(frequency.values(), reverse=True)

ans = 0

for f in frequencies:
    take = min(f, k)
    ans += take * take
    k -= take

    if k == 0:
        break

print(ans)