
def mark_call(val):
    for i, sheet in enumerate(sheets):
        for j, row in enumerate(sheet):
            for k, v in enumerate(row):
                if v == val:
                    call_sheets[i][j][k] = True


def check_bingo():
    winners = set()
    for i, sheet in enumerate(call_sheets):
        # row check
        for row in sheet:
            if sum(row) == 5:
                winners.add(i)
        # col check
        for p, col in enumerate(range(5)):
            if sum([sheet[row][col] for row in range(5)]) == 5:
                winners.add(i)

    return winners


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


pools = set()
for b in balls:
    mark_call(b)
    winners = check_bingo()
    pools = pools | winners
    if len(pools) == 99:
        for i in range(100):
            if i not in winners:
                last_winner = i
                print("last_winner", i)
    if len(pools) == 100:
        total = check_score(last_winner)
        ans = total * b
        print(b, ans)
        break
    # if end_game:
    #     print("ball", b)
    #     total = check_score(winner)
    #     print(total)
    #     ans = total * b
    #     print(b, ans)
    #     break
