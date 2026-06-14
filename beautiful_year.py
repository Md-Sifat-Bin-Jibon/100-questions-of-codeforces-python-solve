year = int(input())

while True:
    year += 1

    syear = str(year)

    if len(set(syear)) == 4:
        print(year)
        break