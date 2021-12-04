import numpy as np


class Player():
    """ A class to represent a bingo player.

    Attributes:
        card -- 2d array representing the current state of the player's bingo card.

        number -- the called number that the player heard last.
        
        score -- the sum of the non-marked squares on the player's board multiplied
        by the last called number.

        winner -- Boolean indicating whether the player has marked a winning line
        on their card.

    Methods:
        mark -- mark the called number if it is on the player's card.
    """

    def __init__(self, card):
        self.number = 0
        self.card = card
        self.card.extend(np.transpose(self.card))

    def mark(self, number):
        self.number = number
        self.card = [[square for square in row if square != self.number] for row in self.card]

    def get_score(self):
        return(self.number * sum(map(sum, self.card)) / 2)

    def get_winner(self):
        for row in self.card:
            if len(row) == 0:
                return(True)
        return(False)

    score = property(get_score)
    winner = property(get_winner)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def play(calls):
    for call in calls:
        for player in players:
            player.mark(call)
            if player.winner:
                return(player.score)

lines = []
with open('inputs/day4-input', 'r') as input:
    for line in input:
        if line.strip():
            lines.append(line.split())

calls = list(map(int, "".join(lines.pop(0)).split(",")))
lines = [list(map(int, line)) for line in lines]
cards = list(chunks(lines, len(lines[0])))
players = [Player(card) for card in cards]

result = play(calls)

print()
print(f"{result}")
print()
