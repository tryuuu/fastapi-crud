from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse
from database import get_db

DbDependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/items", tags=["items"])

@router.get("", response_model=list[ItemResponse], status_code=status.HTTP_200_OK) 
async def find_all(db: DbDependency):
    return item_cruds.find_all(db) # find_all関数でDBセッションを利用できるようになる

@router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK) # idが存在しない場合は404に
async def find_by_id(db: DbDependency, id: int=Path(gt=0)): # idは1以上
    found_item = item_cruds.find_by_id(db, id)
    if found_item is None:
        raise HTTPException(status_code=404, detail="Item not found") 
    return found_item

# パスパラメータと指定されていない引数はクエリパラメータとして扱われる
@router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK) # リストが空でもバリデーションは通る
async def find_by_name(db: DbDependency, name: str=Query(min_length=2, max_length=20)): # nameは2文字以上20文字以下
    return item_cruds.find_by_name(db, name)

@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED) # 作成成功時は201を返す
async def create(db: DbDependency, item_create: ItemCreate): 
    return item_cruds.create(db, item_create)

@router.put("/{id}", response_model=ItemResponse)
async def update(db: DbDependency, item_update: ItemUpdate, id: int=Path(gt=0), status_code=status.HTTP_200_OK): 
    updated_item = item_cruds.update(db, id, item_update)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
async def delete(db: DbDependency, id: int=Path(gt=0)):
    deleted_item = item_cruds.delete(db, id)
    if deleted_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_item