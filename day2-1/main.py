commands = []
with open("part3/input.txt", "r") as f:
    for line in f:
        action, val = line.split(" ")
        commands.append([action, int(val)])

depth = 0
forward = 0
for (action, val) in commands:
    if action == "forward":
        forward += val
    elif action == "up":
        depth -= val
    elif action == "down":
        depth += val

print(depth * forward)
