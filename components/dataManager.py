import json

coins_file = "./data/supportedCoins.json"
inventory = "./data/inventory.json"


def open_file(file):
    with open(file) as f:
        local_data = f.read()
    return json.loads(local_data)


def update_file(location, new_data):
    with open(inventory) as f:
        data = json.load(f)
        data[location] = new_data
        json.dump(data, open(inventory, "w"), indent=4)


class coins:
    data = open_file(coins_file)
    types = data["Coins"]["Types"]


class drinks:
    data = open_file(inventory)
    types = data["Drinks"]


class available_coins:
    data = open_file(inventory)
    types = data["CoinsStock"]
