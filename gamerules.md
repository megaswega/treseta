To create a Tresetta game. First i will need to define the cards. This should be easy as all cards have only two attributes, maybe three if i decide to use a description.

The two attributes every card has is a color which can be:
    Suite
        Denari
        Bastoni
        Spades
        Coppa
    Number
        1
        2
        3
        4
        5
        6
        7
        8
        11
        12
        13

In a turn, each player plays one card from his hand. The first player decides which color is going to be played. The other player has to answer in the same color, if he has a card of that color in his hand. A hand is won by the player who threw the strongest card of the same suite in which the hand is played.
    The card strength is a bit tricky, as it goes 3-2-1-13-12-11-...-4.
    The points are divided into 3 "belas." 3, 2, 13, 12 and 11 wins 1 bela to the winner of the card. Ace carries a point and 3 belas also make a point.

There are 40 cards in a deck, 10 of each suite. At the start, everybody starts with 10 cards in their hand. Every time a player draws a card from the remaining cards, he has to show it to the other player. The player who won the last round draws first.

As this is my first programming project, the progress will be slow. 