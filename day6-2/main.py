from collections import Counter

DAYS = 256
total = 0


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            fishes = list(map(int, line.split(",")))
    current_states = {}
    next_states = {}
    for i in range(9):
        current_states[i] = fishes.count(i)

    for d in range(DAYS):
        for i in range(9):
            if i != 8:
                next_states[i] = current_states[i + 1]
            else:
                next_states[i] = current_states[0]

        if current_states[0] > 0:
            next_states[6] += current_states[0]
        current_states = next_states
        next_states = {}
    for fish in current_states:
        total += current_states[fish]
    print(total)
