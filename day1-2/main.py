ans = 0
depth_list = []
depth = None
with open("part2/input.txt", "r") as f:
    for line in f:
        depth_list.append(int(line))

for index in range(len(depth_list) - 3):
    if depth_list[index] < depth_list[index + 3]:
        ans += 1
print(ans)
