DAYS = 80

if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            fishes = list(map(int, line.split(",")))
    print(fishes)

    for _ in range(DAYS):
        zero_count = fishes.count(0)
        cnt = len(fishes)
        fishes = [6 if v - 1 == -1 else v - 1 for v in fishes]
        for _ in range(zero_count):
            fishes.extend([8])
        # print(fishes, zero_count)
        print(len(fishes))
