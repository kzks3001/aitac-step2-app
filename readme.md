

## 準備
- aws上でRDSを起動(MySQL)
- `.env`ファイルを作成し下記のパラメータを入れる
  - MYSQL_USER
  - MYSQL_ROOT_PASSWORD
  - MYSQL_HOST_NAME
  - MYSQL_DB_NAME
- `docker compose build && docker compose up`からjupyterを起動
- `localhost:8888`にアクセス
- `setup_rdb.ipynb`を開いて実行し、テーブルを作成

## 動作
### 開発時
```
docker compose build # コンテナイメージビルドされてないなら
docker compose up -d
```

jupyterlab: `localhost:8888`
sqlalchemy: `localhost:8080`

### 実行環境での実行
`docker run --env-file .env aitac-proto`
