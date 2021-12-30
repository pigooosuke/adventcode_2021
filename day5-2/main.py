class Vents():
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.areas = [[0 for _ in range(max_size)] for _ in range(max_size)]

    def draw_line(self, from_x: int, from_y: int, to_x: int, to_y: int):
        y_moment = True
        if from_x > to_x:
            from_x, to_x = to_x, from_x
            from_y, to_y = to_y, from_y
        if from_y > to_y:
            y_moment = False
        # draw x-axis
        if from_y == to_y:
            delta = max(abs(from_x - to_x), abs(from_y - to_y))
            for i in range(delta + 1):
                if y_moment is True:
                    x = from_x + i
                else:
                    x = from_x - i
                y = from_y
                self.areas[x][y] += 1
        # draw y-axis
        elif from_x == to_x:
            delta = max(abs(from_x - to_x), abs(from_y - to_y))
            for i in range(delta + 1):
                if y_moment is True:
                    y = from_y + i
                else:
                    y = from_y - i
                x = from_x
                self.areas[x][y] += 1
        # draw diag
        else:
            delta = max(abs(from_x - to_x), abs(from_y - to_y))
            for i in range(delta + 1):
                if y_moment is True:
                    y = from_y + i
                else:
                    y = from_y - i
                x = from_x + i
                self.areas[x][y] += 1

    def calc_score(self):
        score = 0
        for row in self.areas:
            for val in row:
                if val >= 2:
                    score += 1
        print(score)


if __name__ == "__main__":
    inputs = []
    max_size = 0
    with open("day5/input.txt") as f:
        for line in f:
            from_pos, to_pos = line.strip().split(" -> ")
            from_x, from_y = list(map(int, from_pos.split(",")))
            to_x, to_y = list(map(int, to_pos.split(",")))
            max_size = max([from_x, from_y, to_x, to_y, max_size])
            inputs.append([from_x, from_y, to_x, to_y])
    vents = Vents(max_size + 1)
    print(max_size)
    for d in inputs:
        from_x, from_y, to_x, to_y = d
        vents.draw_line(from_x, from_y, to_x, to_y)
    vents.calc_score()
