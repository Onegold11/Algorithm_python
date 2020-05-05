from collections import deque


def left_card(num):
    deck = deque()

    for i in range(1, num + 1):
        deck.append(i)

    while len(deck) != 1:
        deck.popleft()

        card = deck.popleft()
        deck.append(card)
    print(deck.popleft())


N = int(input())
left_card(N)
