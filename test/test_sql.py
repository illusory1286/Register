# 成功添加
import mysql.connector
# 連線資料庫


com = mysql.connector.connect(
    user="root",
    password="********",
    host="localhost",
    database="account_storage"
)

print("資料庫連線成功")
# 建立cusor物件來對資料庫下指令
cursor = com.cursor()
# 下指令添加
# cursor.execute('insert into product(id,name) values (6,"紅茶")')
# cursor.execute('insert into product(name) values ("花茶")')

# 使用變數
a1 = 123123
p1 = 34535
cursor.execute(
    'insert into account(account,password) values (%s,%s)', (a1, p1)
)
print("添加成功")
# 下指令刪除
# cursor.execute('delete from product(name) values ("紅茶")')
# cursor.execute('delete from product(name) values ("花茶")')
# 確定執行
com.commit()
# 關閉資料庫連線
com.close()
