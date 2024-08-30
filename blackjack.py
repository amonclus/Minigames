import random

class Blackjack:
    PLAYER_BUST = 1
    DEALER_BUST = 2
    PLAYER_WINS = 3
    DEALER_WINS = 4

    def __init__(self):
        self.cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]
        self.playerCards = []
        self.dealerCards = []
        self.winner = 0
        self.playerBust = False

    def deal_card_player(self):
        i = random.randint(0, len(self.cards) - 1)
        self.playerCards.append(self.cards[i])
        del self.cards[i]

    def deal_cards(self):
        # Deal one card to the player
        self.deal_card_player()
        # Deal two cards to the dealer
        for k in range(2):
            index = random.randint(0, len(self.cards) - 1)
            self.dealerCards.append(self.cards[index])
            del self.cards[index]

    #1 means that the dealer has busted, 2 means that the player has busted
    def check_bust_player(self):
        if sum(self.playerCards) > 21:
            return Blackjack.PLAYER_BUST
        return 0

    def check_bust_dealer(self):
        if sum(self.dealerCards) > 21:
            return Blackjack.DEALER_BUST
        return 0

    def check_winner_bust(self):
        bustP = self.check_bust_player()
        bustD = self.check_bust_dealer()

        if bustP == Blackjack.PLAYER_BUST:
            self.winner = Blackjack.DEALER_WINS
        elif bustD == Blackjack.DEALER_BUST:
            self.winner = Blackjack.PLAYER_WINS

    def check_winner(self):
        self.check_winner_bust()

        if sum(self.dealerCards) > sum(self.playerCards):
            self.winner = Blackjack.DEALER_WINS
        else:
            self.winner = Blackjack.PLAYER_WINS

    def print_result(self):
        print("You have: ", self.playerCards)
        print("Dealer has: ", self.dealerCards)
        if self.playerBust:
            print("You Busted!!")
        else:
            if self.winner == Blackjack.DEALER_WINS:
                print("Dealer Won, Try again next time")
            elif self.winner == Blackjack.PLAYER_WINS:
                print("YOU WON!!!")


    def play(self):
        self.deal_cards()
        self.check_winner_bust()

        if self.winner == Blackjack.PLAYER_WINS:
            print("Player wins!")
        elif self.winner == Blackjack.DEALER_WINS:
            print("Dealer wins!")

        while not self.playerBust:
            print(self.playerCards)
            action = input("Do you want to hit or stay: ")
            if action == "hit":
                self.deal_card_player()

                bustP = self.check_bust_player()
                if bustP == Blackjack.PLAYER_BUST:
                    self.playerBust = True
                    self.winner = Blackjack.DEALER_WINS
                    break

            elif action == "stay":
                self.check_winner()
                break
        self.print_result()


game = Blackjack()
game.play()

