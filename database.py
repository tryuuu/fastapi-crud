# DBとの接続設定
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://fastapiuser:fastapipass@0.0.0.0:5432/fleamarket"

# engineを通じて実際のDBとの接続を行う
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DBセッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db # DBセッションを返す
    finally: # 関数を抜ける際に実行される
        db.close()