from item import Item

class List:
    def __init__(self, new_list: list[Item] = list()):
        self.list_items: list[Item] = new_list
    
    def add(self, item: Item):
        self.list_items.append(item)
    
    def delete(self, item: Item):
        if item in self.list_items:
            self.list_items.remove(item)
        else:
            print(f'Item {item} doesn\'t exists in list {self.list_items}')

    def get_as_python_list(self) -> list[Item]:
        return self.list_items
