import copy


def find_frequent(l):
    if l.count("1") == l.count("0"):
        return "1"
    elif l.count("1") > l.count("0"):
        return "1"
    else:
        return "0"


def find_infrequent(l):
    if l.count("1") == l.count("0"):
        return "0"
    elif l.count("1") > l.count("0"):
        return "0"
    else:
        return "1"


inputs = []
memo = dict()
with open("part6/input.txt", "r") as f:
    for line in f:
        inputs.append(line.strip())

oxygen = ""
oxygen_candidates = copy.deepcopy(inputs)
max_digit = len(inputs[0])
for i in range(max_digit):
    del_v = list()
    target_list = [v[i] for v in oxygen_candidates]
    target_val = find_frequent(target_list)
    oxygen += target_val
    for idx, v in enumerate(oxygen_candidates):
        if v[i] != target_val:
            del_v.append(v)
    for v in del_v:
        oxygen_candidates.remove(v)
    if len(oxygen_candidates) == 1:
        oxygen = oxygen_candidates[0]
        break
print(oxygen)

co2 = ""
co2_candidates = copy.deepcopy(inputs)
max_digit = len(inputs[0])
for i in range(max_digit):
    del_v = list()
    target_list = [v[i] for v in co2_candidates]
    target_val = find_infrequent(target_list)
    co2 += target_val
    for idx, v in enumerate(co2_candidates):
        if v[i] != target_val:
            del_v.append(v)
    for v in del_v:
        co2_candidates.remove(v)
    if len(co2_candidates) == 1:
        co2 = co2_candidates[0]
        break
print(co2)

ans = int(oxygen, 2) * int(co2, 2)
print(ans)
