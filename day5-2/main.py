class Vents():
    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size
        self.areas = [[0 for _ in range(x_size)] for _ in range(y_size)]

    def draw_line(self, from_x: int, from_y: int, to_x: int, to_y: int):
        y_moment = True
        if from_x > to_x:
            from_x, to_x = to_x, from_x
        if from_y > to_y:
            from_y, to_y = to_y, from_y
            y_moment = False
        # diag check
        if from_x != to_x and from_y != to_y:
            # diag check
            if from_x == from_y and to_x == to_y:
                print(from_x, from_y, to_x, to_y)
                pass
            else:
                return
        # draw x-axis
        if from_y == to_y:
            for i in range(from_x, to_x + 1, 1):
                self.areas[i][from_y] += 1
        # draw y-axis
        elif from_x == to_x:
            for i in range(from_y, to_y + 1, 1):
                self.areas[from_x][i] += 1
        # draw diag
        else:
            for idx, i in enumerate(range(from_x, to_y + 1, 1)):
                if y_moment is True:
                    self.areas[i][i] += 1
                else:
                    self.areas[i][to_y - idx] += 1

    def calc_score(self):
        score = 0
        for row in self.areas:
            for val in row:
                if val >= 2:
                    score += 1
        print(score)


if __name__ == "__main__":
    inputs = []
    max_x, max_y = 0, 0
    with open("day5/input.txt") as f:
        for line in f:
            from_pos, to_pos = line.strip().split(" -> ")
            from_x, from_y = list(map(int, from_pos.split(",")))
            to_x, to_y = list(map(int, to_pos.split(",")))
            max_x = max([from_x, to_x, max_x])
            max_y = max([from_y, to_y, max_y])
            inputs.append([from_x, from_y, to_x, to_y])
    vents = Vents(max_x, max_y)
    for d in inputs:
        from_x, from_y, to_x, to_y = d
        vents.draw_line(from_x, from_y, to_x, to_y)
    vents.calc_score()
