import re


class part_number:

    def __init__(self, number, row, columns):
        self.number = number
        self.columns = columns
        self.row = row

    # number: int
    # row: int
    # columns: list[int]

    def get_adjacent(self):
        adjacent_cells = []
        adjacent_cells.append((self.row, self.columns[0] - 1))
        adjacent_cells.append((self.row, self.columns[-1] + 1))
        adjacent_cells.append((self.row + 1, self.columns[0] - 1))
        adjacent_cells.append((self.row + 1, self.columns[-1] + 1))
        adjacent_cells.append((self.row - 1, self.columns[0] - 1))
        adjacent_cells.append((self.row - 1, self.columns[-1] + 1))
        for col in self.columns:
            adjacent_cells.append((self.row + 1, col))
            adjacent_cells.append((self.row - 1, col))
        return adjacent_cells


def main():
    # file = open('./day_3_example.txt', 'r')
    file = open('./day_3.txt', 'r')
    row = 0
    parts = []
    while True:
        row = row + 1
        line = file.readline()
        if not line:
            break
        nums_in_line = []
        p = re.compile(r"(\d+)")
        for m in p.finditer(line):
            nums_in_line.append((int(m.start()), m.group()))
        for num in nums_in_line:
            start = num[0]
            columns = []
            for n in range(len(str(num[1]))):
                columns.append(n + start)
            part = part_number(int(num[1]), row, columns)
            parts.append(part)
    file.seek(0)
    row = 0
    total = 0
    gear_ratio = 0
    while True:
        row = row + 1
        line = file.readline()
        if not line:
            break
        for i, letter in enumerate(line):
            if not letter.isalnum() and letter != '.' and letter != '\n':
                position = (row, i)
                gears = []
                for part in parts:
                    if position in part.get_adjacent():
                        gears.append(part.number)
                        total = total + int(part.number)
                if len(gears) == 2:
                    gear_ratio = gear_ratio + (gears[0] * gears[1])
    print(total)
    print(gear_ratio)
    file.close()

main()

