import art
import random

def deal_card():
      """Returns a random card from the deck"""
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      card = random.choice(cards)
      return card

def calculate_score(cards):
      """Take a list of cards and return the score calculated from the cards"""
      if sum(cards) == 21 and len(cards) ==2:
            return 0
      if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

      return sum(cards)

def compare(player, dealer):
      if player == dealer:
            return "Draw"
      elif dealer == 0:
            return "Lose, opponent has Blackjack"
      elif player == 0:
            return "Win with a Blackjack"
      elif player > 21:
            return "You went over. You lose"
      elif dealer > 21:
            return "Dealer went over. You win"
      elif player > dealer:
            return "You win"
      else:
            return "You lose"

def play_game():
      print(art.logo)
      player_cards = []
      dealer_cards = []
      dealer_score = -1
      player_score = -1
      is_game_over = False

      for i in range(0,2):
            player_cards.append(deal_card())
            dealer_cards.append(deal_card())

      while not is_game_over:
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"Your cards: {player_cards}, current score: {player_score}\n"
                  f"Dealer's first card: {dealer_cards[0]}")

            if player_score == 0 or dealer_score == 0 or player_score > 21:
                  is_game_over = True
            else:
                  deal_or_stand = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                  if deal_or_stand == "y":
                        player_cards.append(deal_card())
                  else:
                        while dealer_score != 0 and dealer_score < 17:
                              dealer_cards.append(deal_card())
                              dealer_score = calculate_score(dealer_cards)
                        is_game_over= True

      print(f"Your final hand: {player_cards}, final score: {player_score}")
      print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
      print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
      print("\n" *30)
      play_game()