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




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    day_one_part_1()
    day_one_part_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
