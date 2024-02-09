import copy
import numpy as np

from pymongo import MongoClient


class Player:
    def __init__(self, name, max_health, max_energy, items=[]):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.energy = max_energy
        self.max_energy = max_energy
        self.items = copy.deepcopy(items)

    def attack(self, player):
        energy_cost = 5

        if self.energy >= energy_cost:
            attack_strength = np.random.randint(1, 6)
            player.health -= attack_strength
            self.energy -= energy_cost
            print("{} attacked {} for {} damage".format(self.name, player.name, attack_strength))
        else:
            print("{} does not have enough energy to attack {}".format(self.name, player.name))

    def heal(self, amount):
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health

    def stats(self):
        return vars(self)

    def use_item(self, item_name):
        try:
            item = next(item for item in self.items if item.name == item_name)
            item.quantity -= 1

            for effect in item.effects:

                for method, value in effect.items():
                    class_method = getattr(self, method)
                    class_method(value)

            if item.quantity == 0:
                self.items.remove(item)

        except:
            print("{} does not have any {}s".format(self.name, item_name))


class Item:
    def __init__(self, name, quantity, effects=[]):
        self.name = name
        self.quantity = quantity
        self.effects = effects

    def __repr__(self):
        return "Item(name={}, quantity={}, effects={})".format(self.name, self.quantity, self.effects)

client = MongoClient('mongodb://localhost:27017/')
db = client['video_game']


# TODO:
# 2) Create a function that takes in a Player object and inserts it into the database,
#    Extra Challenge: check for duplicate player entries, if so, do not insert again
def insert_player(player_obj, check_for_duplicates=True):

    if check_for_duplicates:
        duplicate_player = db.players.find_one({"name": player_obj.name})
        if duplicate_player != None:
            return duplicate_player["_id"]


    player_dict = copy.deepcopy(vars(player_obj))
    print(player_dict)
    items_dict_list = []
    for item_obj in player_dict["items"]:
        item_dict = vars(item_obj)
        items_dict_list.append(item_dict)

    player_dict["items"] = items_dict_list
    print(items_dict_list)
    return db.players.insert_one(player_dict).inserted_id


# 3) Create a function that is able to find a Player in the databse by searching for their name
def find_player_by_name(name):
    return db.players.find_one({"name": name})


# 4) Create a function that loads the data from the above function and returns a Player object configured with that data
def convert_player_dict_to_obj(player_dict):
    p = player_dict

    items_list = []
    for item in p["items"]:
        item_obj = Item(item["name"], item["quantity"], item["effects"])
        items_list.append(item_obj)

    player_obj = Player(p["name"], p["max_health"], p["max_energy"], items_list)
    player_obj.health = p["health"]
    player_obj.energy = p["energy"]

    return player_obj


def get_player_obj_by_name(name):
    player_dict = find_player_by_name(name)
    return convert_player_dict_to_obj(player_dict)

# TODO:
# 5) Create at least 2 players, optionally give them items
player1_items = [Item("health_potion", 2, [{"heal": 10}])]
player1 = Player("Maximuss", 50, 25, player1_items)

player2_items = [Item("greater_health_potion", 2, [{"heal": 25}])]
player2 = Player("Sophie", 60, 35, player2_items)


# 6) Insert Players into MongoDB
player1_id = insert_player(player1)
player2_id = insert_player(player2)
