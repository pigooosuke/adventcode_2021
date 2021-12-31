areas = []
points = 0

if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f:
            row = [float("inf")] + [int(v)
                                    for v in line.strip()] + [float("inf")]
            areas.append(row)
    lowest_peak = list()
    row_max = len(areas)
    col_max = len(areas[0])
    print(row_max, col_max)
    areas = [[float("inf")] * col_max] + areas + [[float("inf")] * col_max]
    print(areas)
    for i in range(1, row_max + 1):
        for j in range(1, col_max - 1):
            # print(i, j)
            print(areas[i][j])
            if areas[i][j] < min(areas[i - 1][j],
                                 areas[i + 1][j],
                                 areas[i][j - 1],
                                 areas[i][j + 1]):
                lowest_peak.append(areas[i][j])
    print(lowest_peak)
    for v in lowest_peak:
        points += v + 1
    print(points)
