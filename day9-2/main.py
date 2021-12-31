areas = []
points = 0

if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            row = [0 if v == "9" else 1 for v in line.strip()]
            areas.append(row)
    print(areas)
    seen = set()

    def area(r, c):
        if not (0 <= r < len(areas) and 0 <= c < len(areas[0])
                and (r, c) not in seen and areas[r][c]):
            return 0
        seen.add((r, c))
        return (
            1 +
            area(r + 1, c) +
            area(r - 1, c) +
            area(r, c - 1) +
            area(r, c + 1))
    group = sorted([area(r, c) for r in range(len(areas))
                    for c in range(len(areas[0]))])
    ans = 1
    for v in group[-3:]:
        ans *= v
    print(group[-3:])
    print(ans)
