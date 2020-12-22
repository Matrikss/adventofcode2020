player1_cards = [30, 42, 25, 7, 29, 1, 16, 50, 11, 40, 4, 41, 3, 12, 8, 20, 32, 38, 31, 2, 44, 28, 33, 18, 10]
player2_cards = [36, 13, 46, 15, 27, 45, 5, 19, 39, 24, 14, 9, 17, 22, 37, 47, 43, 21, 6, 35, 23, 48, 34, 26, 49]

round = 1
while len(player1_cards) > 0 and len(player2_cards) > 0:
    if player1_cards[0] > player2_cards[0]:
        player1_cards.append(player1_cards.pop(0))
        player1_cards.append(player2_cards.pop(0))
    else:
        player2_cards.append(player2_cards.pop(0))
        player2_cards.append(player1_cards.pop(0))
    round += 1

part_1 = 0
player1_cards.reverse()
player2_cards.reverse()
for i, x in enumerate(player1_cards):
    part_1 += x * (i + 1)
for i, x in enumerate(player2_cards):
    part_1 += x * (i + 1)

print(part_1)
