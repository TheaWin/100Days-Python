import art
print(art.logo)

status = True
auction = {}

def highest_bidder(auction_dictionary):
    winner = ""
    highest_bid = 0
    for i in auction_dictionary:
        bid_amount = auction_dictionary[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The highest bidder is {winner} with ${highest_bid}")

while status:
    name = input("What is your name?:")
    bid = int(input("What's your bid?:"))
    more = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    auction[name] = bid
    if more == "no":
        status = False
        highest_bidder(auction)
    else:
        print("\n" * 20)
