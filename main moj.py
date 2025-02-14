import random
# stavaljanje svih karata u deck
def builddeck():
    deck = []
    boje = ["S", "K", "D", "B"]
    values = [1,2,3,4,5,6,7,11,12,13]
    for boja in boje:
        for broj in values:
            cardval = "{}{}".format(boja, broj)
            deck.append(cardval)
    return deck
deck = builddeck()
#shufflanje
def shuffledeck(deck):
    for cardpos in range(len(deck)):
        randPos = random.randint(0,39)
        deck[cardpos], deck[randPos] = deck[randPos], deck [cardpos]
    return deck
gotovdeck = shuffledeck(deck)
print(gotovdeck)