commands = []
with open("part4/input.txt", "r") as f:
    for line in f:
        action, val = line.split(" ")
        commands.append([action, int(val)])

aim = 0
pos = 0
depth = 0
for (action, val) in commands:
    if action == "forward":
        pos += val
        depth += aim * val
    elif action == "up":
        aim -= val
    elif action == "down":
        aim += val
print(pos * depth)
