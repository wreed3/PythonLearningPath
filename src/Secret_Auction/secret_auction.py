from secret_auction_logo import secret_auction_logo

print(secret_auction_logo)

bidders = True
bids = []

max_bid = {
    "name": "",
    "bid": 0
}
winner = {}
while bidders:
    name = input("What is your name?: ")
    bid = (int(input("What's your bid?: $ ")))
    bids.append({"name": name, "bid": bid})
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    while 'no' != more_bidders != 'yes':
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if more_bidders == 'yes':
        bidders = True
    else:
        bidders = False
        for index, bid in enumerate(bids):
            if max_bid["bid"] > bids[index]["bid"]:
                max_bid = max_bid
            else:
                max_bid = bids[index]
    print("\n" * 70)
print(f"The winner is {max_bid["name"].capitalize()} with a bid of ${max_bid["bid"]}")