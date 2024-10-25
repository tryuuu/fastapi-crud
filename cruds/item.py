from sqlalchemy.orm import Session
from typing import Optional
from schemas import ItemCreate, ItemStatus, ItemUpdate
from models import Item

"""class Item:
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
]"""

def find_all(db: Session):
    return db.query(Item).all()

def find_by_id(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()

def find_by_name(db: Session, name: str):
    return db.query(Item).filter(Item.name.like(f"%{name}%")).all() # 複数レコードの可能性がある

def create(db: Session, item_create: ItemCreate):
    # Itemインスタンスを作成(DBのモデル)
    new_item = Item(
        **item_create.model_dump()
    )
    db.add(new_item) # DBセッションに追加
    db.commit() # コミットして保存
    return new_item

def update(db: Session, id: int, item_update: ItemUpdate):
    item = find_by_id(db, id)
    if item is None:
        return None
    item.name = item.name if item_update.name is None else item_update.name
    item.price = item_update.price if item_update.price is None else item_update.price
    item.description = item_update.description if item_update.description is None else item_update.description
    item.status = item_update.status if item_update.status is None else item_update.status
    db.add(item)
    db.commit()
    return item


def delete(db: Session, id: int):
    item = find_by_id(db, id)
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item