
def incremental(val: int):
    total = 0
    for i in range(1, val + 1):
        total += i
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            crabs = list(map(int, line.split(",")))
    crabs.sort()
    start_val = crabs[len(crabs) // 2]
    print(crabs)
    loss = float("inf")
    tmp_v = start_val
    print(tmp_v)
    while tmp_v < crabs[-1]:
        new_loss = sum([incremental(abs(v - tmp_v)) for v in crabs])

        # print(loss, tmp_v)
        if loss < new_loss:
            print(loss, new_loss, tmp_v)
            break
        loss = new_loss
        tmp_v += 1

    tmp_v = start_val - 1
    while tmp_v > crabs[0]:
        new_loss = sum([incremental(abs(v - tmp_v)) for v in crabs])
        # print(loss, tmp_v)
        if loss < new_loss:
            print(loss, new_loss, tmp_v)
            tmp_v += 1
            break
        loss = new_loss
        tmp_v -= 1
    print("ans:", loss, tmp_v)
