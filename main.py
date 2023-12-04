# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def day_one_part_1():
    file = open('./input_files/day_1.txt', 'r')
    total = 0
    while True:
        content = file.readline()
        nums = []
        if not content:
            break
        for character in content:
            if character.isnumeric():
                nums.append(character)
        number_string = nums[0] + nums.pop()
        total = total + int(number_string)
    file.close()
    print(total)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches

def day_one_part_2():
    number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    file = open('./input_files/day_1.txt', 'r')
    # file = open('./input_files/day_1_example.txt', 'r')
    total = 0
    while True:
        content = file.readline()
        if not content:
            break
        indexes = []
        for i, letter in enumerate(content):
            if letter.isnumeric():
                indexes.append((i, int(letter)))
        for i, x in enumerate(number_strings):
            idxs = find_all(content, x)
            for idx in list(idxs):
                if idx != -1:
                    indexes.append((idx, number_strings.index(x)+1))
        indexes.sort()
        x = str(indexes[0][1]) + str(indexes.pop()[1])
        total = total + int(x)
    file.close()
    print(total)


class Round:
    def __init__(self, red, green, blue):
        self.green = green
        self.red = red
        self.blue = blue
    green: int
    red: int
    blue: int

    def is_valid(self, red, green, blue):
        if self.green > green:
            return False
        if self.blue > blue:
            return False
        if self.red > red:
            return False
        return True


class Game:
    def __init__(self, id, rounds):
        self.id = id
        self.rounds = rounds

    id: int
    rounds: list[Round]

    def is_valid(self, red, green, blue):
        valid = True
        for r in self.rounds:
            if not r.is_valid(red, green, blue):
                valid = False
        return valid
def day_two_part_1():
    # file = open('./input_files/day_2_example.txt', 'r')
    file = open('./input_files/day_2.txt', 'r')
    red_max = 12
    green_max = 13
    blue_max = 14
    total = 0
    while True:
        content = file.readline()
        if not content:
            break
        id = int(content.split(':')[0].split(' ')[1])
        rounds = content.split(':')[1].split(';')
        valid = True
        for r in rounds:
            colors = r.split(',')
            for color in colors:
                match color.split(' ')[2].rstrip('\n'):
                    case 'blue':
                        if int(color.split(' ')[1]) > blue_max:
                            valid = False
                    case 'red':
                        if int(color.split(' ')[1]) > red_max:
                            valid = False
                    case 'green':
                        if int(color.split(' ')[1]) > green_max:
                            valid = False
                    case _:
                        print('invalid color')
                        print(colors)
                        print(color)
        if valid:
            total = total + id
    print(total)

def day_two_part_2():
    # file = open('./input_files/day_2_example.txt', 'r')
    file = open('./input_files/day_2.txt', 'r')
    total = 0
    while True:
        content = file.readline()
        if not content:
            break
        rounds = content.split(':')[1].split(';')
        blue_min = 0
        red_min = 0
        green_min = 0
        for r in rounds:
            colors = r.split(',')
            for color in colors:
                match color.split(' ')[2].rstrip('\n'):
                    case 'blue':
                        if int(color.split(' ')[1]) > blue_min:
                            blue_min = int(color.split(' ')[1])
                    case 'red':
                        if int(color.split(' ')[1]) > red_min:
                            red_min = int(color.split(' ')[1])
                    case 'green':
                        if int(color.split(' ')[1]) > green_min:
                            green_min = int(color.split(' ')[1])
                    case _:
                        print('invalid color')
                        print(colors)
                        print(color)
        print('power: ' + str(red_min * blue_min * green_min))
        total = total + (red_min * blue_min * green_min)
    print(total)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # day_one_part_1()
    # day_one_part_2()
    # day_two_part_1()
    day_two_part_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

