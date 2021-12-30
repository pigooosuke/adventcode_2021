
def mark_call(val):
    for i, sheet in enumerate(sheets):
        for j, row in enumerate(sheet):
            for k, v in enumerate(row):
                if v == val:
                    call_sheets[i][j][k] = True


def check_bingo():
    end_game = False
    winner = None
    for i, sheet in enumerate(call_sheets):
        # row check
        for row in sheet:
            if sum(row) == 5:
                end_game = True
                winner = i
        # col check
        for p, col in enumerate(range(5)):
            if sum([sheet[row][col] for row in range(5)]) == 5:
                end_game = True
                winner = i

    return end_game, winner


def check_score(winner):
    total = 0
    for idx, row in enumerate(sheets[winner]):
        for col, v in enumerate(row):
            if call_sheets[winner][idx][col] == False:
                total += v
    return total


# input
with open("day4/input.txt", "r") as f:
    contents = f.read()[:-1].split("\n\n")
    balls = contents[0]
    balls = list(map(int, balls.split(",")))
    tmp_sheets = contents[1:]

sheets = list()
for s in tmp_sheets:
    tmp_sheet = list()
    for row in s.split("\n"):
        row = list(map(int, row.split()))
        tmp_sheet.append(row)
    sheets.append(tmp_sheet)
del tmp_sheets


call_sheets = [
    [[False * 5 for _ in range(5)] for _ in range(5)] for _ in range(len(sheets))]


for b in balls:
    mark_call(b)
    end_game, winner = check_bingo()
    if end_game:
        print("ball", b)
        total = check_score(winner)
        print(total)
        ans = total * b
        print(b, ans)
        break
