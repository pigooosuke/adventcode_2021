from collections import Counter
from os import initgroups
total = 0

# word counts from 0 to 9
# A:8
# B:6 -- unique
# C:8
# D:7
# E:4 -- unique
# F:9 -- unique
# G:7

INT_CODES = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            codes = {}
            digit_head, digit_tail = line.strip().split("|")
            inputs = digit_head.strip().split(" ")
            outputs = digit_tail.strip().split(" ")
            inputs_cnt = Counter("".join(inputs))
            # word counts
            for k, v in inputs_cnt.items():
                if v == 6:
                    codes["b"] = k
                elif v == 4:
                    codes["e"] = k
                elif v == 9:
                    codes["f"] = k
            # words len
            inputs_digit = [len(v) for v in inputs]
            # find 1
            one_words = inputs[inputs_digit.index(2)]
            for v in one_words:
                if v not in list(codes.values()):
                    codes["c"] = v
                    break
            # find 7
            seven_words = inputs[inputs_digit.index(3)]
            for v in seven_words:
                if v not in list(codes.values()):
                    codes["a"] = v
                    break
            # find 4
            four_words = inputs[inputs_digit.index(4)]
            for v in four_words:
                if v not in list(codes.values()):
                    codes["d"] = v
                    break
            # last char
            for v in "abcdefg":
                if v not in list(codes.values()):
                    codes["g"] = v
                    break
            codes_inv = {v: k for k, v in codes.items()}
            total_str = ""
            for v in outputs:

                tmp_output = sorted([codes_inv[w] for w in v])
                output_values = "".join(tmp_output)
                vs = INT_CODES[output_values]
                total_str += vs
            total += int(total_str)

    print(total)
