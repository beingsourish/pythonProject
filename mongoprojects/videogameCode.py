import copy
from pymongo import mongo_client
import pymongoscript as pp

class players:
    def __init__(self,name,health,energy,items=[]):
        self.name=name
        self.health = health
        self.energy = energy
        self.items = items

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.name}, y={self.health})"


class Item:
    def __init__(self, name, quantity, effects=[]):
        self.name = name
        self.quantity = quantity
        self.effects = effects

    def __repr__(self):
        return "Item(name={}, quantity={}, effects={})".format(self.name, self.quantity, self.effects)

def get_count_by_name(coll,name):
    return coll.count_documents({"name":name})

def insert_player(p,player_items,coll):
    counts=get_count_by_name(coll,p.name)
    #print(counts)
    if counts==0:
        player_dict={}
        p_list=[]
        player_dict["name"]=p.name
        player_dict["health"] = p.health
        player_dict["energy"] = p.energy
        #print(player_dict)
        #print(player_items)
        #print(vars(player_items))
        player_dict_v2 = (vars(p))
        print(player_dict_v2)
        print(player_dict_v2['items'])
        for r in player_dict_v2['items']:

            p_list.append(vars(r))
            print(p_list)
        player_dict["items"] = p_list
        print(player_dict)
        pp.insert_data_coll(coll,player_dict)
    else:
        print("Same User Exists Already")

conn=pp.get_connection()
#print(conn)
coll=pp.get_db_details(conn)
player1_items = [Item("health_potion", 2, [{"heal": 10}])]
p = players("champ", "5", "10",player1_items)
#print(vars(p))
insert_player(p,player1_items,coll)