from list import List
from item import Item

item1 = Item("do the dishes")
item2 = Item("listen to music")
item3 = Item("setup git")
item4 = Item("wake up")

user1 = List([item1, item2, item3, item4, Item("eat"), Item("sleep"), Item("code this thing right")])

user1.list_items[1].set_is_done(True)
user1.list_items[3].set_is_done(True)
user1.list_items[4].set_is_done(True)
