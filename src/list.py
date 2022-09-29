from item import Item

class List:
    def __init__(self, existing_list=None):
        if existing_list is None:
            self.list_items = list()
        else:
            self.list_items = list(existing_list)
    
    def add(self, item: Item):
        self.list_items.append(item)
    
    def delete(self, item: Item):
        if item in self.list_items:
            self.list_items.delete(item)
        else:
            print(f'Item {item} doesn\'t exists in list {self.list_items}')

    def get_as_python_list(self) -> list:
        return self.list_items