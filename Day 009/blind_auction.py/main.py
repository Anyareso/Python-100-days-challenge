# from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
auction_details = {}
bidding_finished = False

def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    # bid_record = {"Agnes":124, "James":908}
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_details[name] = bid
    should_continue = input("Are there any other bidder? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(auction_details)
    elif should_continue == "yes":
        print("\033c", end='')
    


