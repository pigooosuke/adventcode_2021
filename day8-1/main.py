total = 0

if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            digit_head, digit_tail = line.split("|")
            outputs = digit_tail.strip().split(" ")
            # print(outputs)
            outputs_digit = [len(v) for v in outputs]
            total += len([v for v in outputs_digit if v in (2, 3, 4, 7)])
    print(total)
