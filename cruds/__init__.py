from enum import Enum
from typing import Optional
# Item
class ItemStatus(Enum):
    ON_SALE = "ON"
    SOLD_OUT = "SOLD_OUT"
class Item:
    # コンストラクタ
    def __init__(
        self,
        id: int,
        name: str,
        price: int,
        description: Optional[str], # オプショナル
        status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status

items = [
    Item(1,"PC",10000,"備品です",ItemStatus.ON_SALE),
    Item(2,"スマホ",50000,"備品です",ItemStatus.ON_SALE),
    Item(3,"タブレット",30000,"使用感あり",ItemStatus.SOLD_OUT),
]

def find_all():
    return items
