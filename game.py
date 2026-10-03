from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
        print("Dealer:", " ".join(shown_dealer))
        print("Player:", " ".join(f"{r}{s}" for r, s in player),
              "=", hand_value(player))

    def settle(self, result, wager):
        if result == "win":
            self.chips += wager
            print("Player wins.")
        elif result == "lose":
            self.chips -= wager
            print("Dealer wins.")
        else:
            print("Push.")

    def round(self):
        print("Chips:", self.chips)
        while True:
            raw = input("Wager: ").strip().lower()
            if raw == "q":
                return False
            try:
                wager = int(raw)
            except ValueError:
                print("Invalid wager.")
                continue
            if wager <= 0 or wager > self.chips:
                print("Invalid wager.")
                continue
            break

        deck = Deck()
        player = [deck.draw(), deck.draw()]
        dealer = [deck.draw(), deck.draw()]
        self.show(player, dealer)

        player_blackjack = len(player) == 2 and hand_value(player) == 21
        dealer_blackjack = len(dealer) == 2 and hand_value(dealer) == 21

        if player_blackjack or dealer_blackjack:
            self.show(player, dealer, hide=False)
            if player_blackjack and dealer_blackjack:
                self.settle("push", wager)
            elif player_blackjack:
                self.settle("win", wager)
            else:
                self.settle("lose", wager)
            return True

        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()
            if key == "q":
                return False
            if key == "s":
                break
            if key == "h":
                player.append(deck.draw())
                self.show(player, dealer)
                if hand_value(player) > 21:
                    print("Player busts.", end=" ")
                    self.settle("lose", wager)
                    return True

        while hand_value(dealer) < 17:
            dealer.append(deck.draw())

        self.show(player, dealer, hide=False)
        pv, dv = hand_value(player), hand_value(dealer)
        if dv > 21 or pv > dv:
            self.settle("win", wager)
        elif pv < dv:
            self.settle("lose", wager)
        else:
            self.settle("push", wager)
        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)
        while self.chips > 0:
            if not self.round():
                return
            if self.chips == 0:
                print("Out of chips. Game over.")
                return
            if input("Play again? [y/n]: ").strip().lower() != "y":
                return
                
# Original Code

# from cards import Deck, hand_value


# class Blackjack:
#     def __init__(self):
#         self.chips = 100

#     def show(self, player, dealer, hide=True):
#         shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
#         print("Dealer:", " ".join(shown_dealer))
#         print("Player:", " ".join(f"{r}{s}" for r, s in player),
#               "=", hand_value(player))

#     def round(self):
#         deck = Deck()
#         player = [deck.draw(), deck.draw()]
#         dealer = [deck.draw(), deck.draw()]
#         self.show(player, dealer)

#         while hand_value(player) < 21:
#             key = input("[h]it [s]tand [q]uit: ").strip().lower()
#             if key == "q":
#                 return False
#             if key == "s":
#                 break
#             if key == "h":
#                 player.append(deck.draw())
#                 self.show(player, dealer)
#                 if hand_value(player) > 21:
#                     print("Bust.")
#                     return True
#         while hand_value(dealer) < 17:
#             dealer.append(deck.draw())

#         self.show(player, dealer, hide=False)
#         pv, dv = hand_value(player), hand_value(dealer)
#         if dv > 21 or pv > dv:
#             self.chips += 10
#             print("Player wins.")
#         elif pv < dv:
#             self.chips -= 10
#             print("Dealer wins.")
#         else:
#             print("Push.")
#         return True

#     def run(self):
#         print("Blackjack — starting chips:", self.chips)
#         while self.chips > 0:
#             if not self.round():
#                 return
#             if input("Play again? [y/n]: ").strip().lower() != "y":
#                 return

# Task 2 - Fix (First Version)
# from cards import Deck, hand_value


# class Blackjack:
#     def __init__(self):
#         self.chips = 100

#     def show(self, player, dealer, hide=True):
#         shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
#         print("Dealer:", " ".join(shown_dealer))
#         print("Player:", " ".join(f"{r}{s}" for r, s in player),
#               "=", hand_value(player))

#     def round(self):
#         deck = Deck()
#         player = [deck.draw(), deck.draw()]
#         dealer = [deck.draw(), deck.draw()]
#         self.show(player, dealer)

#         player_blackjack = len(player) == 2 and hand_value(player) == 21
#         dealer_blackjack = len(dealer) == 2 and hand_value(dealer) == 21

#         if player_blackjack or dealer_blackjack:
#             self.show(player, dealer, hide=False)
#             if player_blackjack and dealer_blackjack:
#                 print("Push.")
#             elif player_blackjack:
#                 self.chips += 10
#                 print("Player wins.")
#             else:
#                 self.chips -= 10
#                 print("Dealer wins.")
#             return True

#         while hand_value(player) < 21:
#             key = input("[h]it [s]tand [q]uit: ").strip().lower()
#             if key == "q":
#                 return False
#             if key == "s":
#                 break
#             if key == "h":
#                 player.append(deck.draw())
#                 self.show(player, dealer)
#                 if hand_value(player) > 21:
#                     self.chips -= 10
#                     print("Player busts. Dealer wins.")
#                     return True

#         while hand_value(dealer) < 17:
#             dealer.append(deck.draw())

#         self.show(player, dealer, hide=False)
#         pv, dv = hand_value(player), hand_value(dealer)
#         if dv > 21 or pv > dv:
#             self.chips += 10
#             print("Player wins.")
#         elif pv < dv:
#             self.chips -= 10
#             print("Dealer wins.")
#         else:
#             print("Push.")
#         return True

#     def run(self):
#         print("Blackjack — starting chips:", self.chips)
#         while self.chips > 0:
#             if not self.round():
#                 return
#             if input("Play again? [y/n]: ").strip().lower() != "y":
#                 return

# Task 2 - Fix (Version 2 - Complete Round)
# from cards import Deck, hand_value


# class Blackjack:
#     def __init__(self):
#         self.chips = 100

#     def show(self, player, dealer, hide=True):
#         shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
#         print("Dealer:", " ".join(shown_dealer))
#         print("Player:", " ".join(f"{r}{s}" for r, s in player),
#               "=", hand_value(player))

#     def settle(self, result):
#         if result == "win":
#             self.chips += 10
#             print("Player wins.")
#         elif result == "lose":
#             self.chips -= 10
#             print("Dealer wins.")
#         else:
#             print("Push.")

#     def round(self):
#         deck = Deck()
#         player = [deck.draw(), deck.draw()]
#         dealer = [deck.draw(), deck.draw()]
#         self.show(player, dealer)

#         player_blackjack = len(player) == 2 and hand_value(player) == 21
#         dealer_blackjack = len(dealer) == 2 and hand_value(dealer) == 21

#         if player_blackjack or dealer_blackjack:
#             self.show(player, dealer, hide=False)
#             if player_blackjack and dealer_blackjack:
#                 self.settle("push")
#             elif player_blackjack:
#                 self.settle("win")
#             else:
#                 self.settle("lose")
#             return True

#         while hand_value(player) < 21:
#             key = input("[h]it [s]tand [q]uit: ").strip().lower()
#             if key == "q":
#                 return False
#             if key == "s":
#                 break
#             if key == "h":
#                 player.append(deck.draw())
#                 self.show(player, dealer)
#                 if hand_value(player) > 21:
#                     print("Player busts.", end=" ")
#                     self.settle("lose")
#                     return True

#         while hand_value(dealer) < 17:
#             dealer.append(deck.draw())

#         self.show(player, dealer, hide=False)
#         pv, dv = hand_value(player), hand_value(dealer)
#         if dv > 21 or pv > dv:
#             self.settle("win")
#         elif pv < dv:
#             self.settle("lose")
#         else:
#             self.settle("push")
#         return True

#     def run(self):
#         print("Blackjack — starting chips:", self.chips)
#         while self.chips > 0:
#             if not self.round():
#                 return
#             if input("Play again? [y/n]: ").strip().lower() != "y":
#                 return
