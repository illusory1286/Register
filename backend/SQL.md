<h1>SQＬ語法
<h3>創建(create)database

```SQL
create database {Name};
```
<h3>刪除(drop)database

```SQL
drop database {Name};
```

<h3>顯示(show)database

```SQL
show database {Name};
```

<h3>將資料寫入 MySQL 資料庫
<h4>使用變數能防止SQL injection

```python
query = "INSERT INTO account (account,password) VALUES (%s, %s)"
values = (account, password)
cursor.execute(query, values)
db.commit()
```