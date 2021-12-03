ans = 0
depth = None
with open("part1/input.txt", "r") as f:
    for line in f:
        if depth is None:
            tmp_depth = int(line)
            depth = int(line)
            continue
        tmp_depth = int(line)
        if depth < tmp_depth:
            ans += 1
        depth = int(line)
print(ans)
