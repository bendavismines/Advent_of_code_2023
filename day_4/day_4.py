import cProfile
import bisect

pr = cProfile.Profile()


class Card:
    def __init__(self, number, winners, mine):
        self.number = number
        self.winners = winners
        self.mine = mine
        self.overlap = len(set(winners) & set(mine))

    number: int
    winners: list[int]
    mine: list[int]
    overlap: int

    # overlap: set[int]

    def score(self):
        if self.overlap == 0:
            return 0
        else:
            return 2 ** (self.overlap - 1)


def score_copies(cards: list[Card]):
    total = 0
    pr.enable()
    for card in cards:
        total = recurse_(card, total)
    pr.disable()
    return total


def recurse_(card, running_total):
    running_total = running_total + 1
    if card.overlap == 0:
        return running_total
    else:
        for i in range(card.overlap):
            next_card = next(x for x in cards if x.number == (i + card.number + 1))
            running_total = recurse_(next_card, running_total)
        return running_total


cards = []


def main():
    # file = open('./day_4_example.txt', 'r')
    file = open('./day_4.txt', 'r')
    total = 0
    while True:
        line = file.readline()
        if not line:
            break
        card_number = int(line.split(':')[0].split(' ')[-1])
        _winners = line.split(':')[1].split('|')[0].split(' ')
        _winners = list(filter(None, _winners))
        _mine = line.split(':')[1].split('|')[1].split(' ')
        _mine = list(filter(None, _mine))
        mine = [eval(i) for i in _mine]
        winners = [eval(i) for i in _winners]
        cards.append(Card(card_number, winners, mine))
    for card in cards:
        score = card.score()
        total = total + score

    print(score_copies(cards))
    print(total)
    pr.print_stats(sort="calls")


main()
