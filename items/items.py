from typing import Protocol

class Item(Protocol):

    item_value: float
    item_name: str
    item_bonus: float
    
    def sell_item(self):
        ...