n = int(input())
a = list(map(int, input().split()))

m= int(input())
b = list(map(int, input().split()))

ratios = []

for a_i in a:
    for b_i in b:
        if b_i % a_i == 0:
            ratios.append(b_i // a_i)
        
mx = max(ratios)
print(ratios.count(mx))