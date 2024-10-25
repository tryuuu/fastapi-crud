## fastapiインストール
仮想環境を作成後、
```
pip install "fastapi[standard]"
```
## main.pyの起動
```
fastapi dev main.py
```

## DB設定
### sqlalchemyとalembicのインストール
```
pip install sqlalchemy
pip install alembic psycopg2-binary
```
### 初期化
```
alembic init migrations
```
### マイグレーション実行
```
alembic revision --autogenerate -m "create items table"
alembic upgrade head
```
