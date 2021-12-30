inputs = []
memo = dict()
with open("part5/input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip())


for val in inputs:
    for i, v in enumerate(val):
        if i not in memo:
            memo[i] = 0
        if int(v) == 1:
            memo[i] += 1
        else:
            memo[i] -= 1
print(memo)
indicator = ""
for i, v in memo.items():
    if v > 0:
        indicator += "1"
    else:
        indicator += "0"
print(indicator)

gamma = int(indicator, 2)
epsilon = ~gamma & 0xfff

ans = gamma * epsilon
print(ans)
