import os
import art

def clear_screen():
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
print(art.logo)
# TODO-1: Ask the user for input

bids = {}
winner={}


def bid_collector():
    """Collects bid information from the user."""
    name = input("Enter your name: ")
    bid = float(input("Enter your bid amount: $"))

    bids[name] = bid  # Store the bid


while True:
    bid_collector()

    reset = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if reset == "yes":
        clear_screen()  # Clears screen
    elif reset == "no":
        break  # Stop asking

# Find the winner
if bids:
    winner = max(bids, key=bids.get)
    highest_bid = bids[winner]

    clear_screen()
    print(f"Auction Winner: {winner} with a bid of ${highest_bid:.2f}")
else:
    print("No bids were placed.")



