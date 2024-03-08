import mysql.connector
from config import db  # 引用資料庫配置文件
# 連線資料庫
# com = mysql.connector.connect(
#     user="root",
#     password="W8i4n1d24~",
#     host="localhost",
#     database="account_storage"
# )

print("資料庫連線成功")
# 建立cusor物件來對資料庫下指令
cursor = db.cursor()

# 取得單一資料
# cursor.execute('SELECT * FROM product where id =2')
# data_one = cursor.fetchone()
# print(type(data_one))
# # 分開取出
# print(data_one[0], data_one[1])

# 取得所有数据库数据
# cursor.execute('SELECT * FROM account')
# # 獲取所有数据
# data_all = cursor.fetchall()
# print(data_all)
# # 逐一取得資料
# for row in data_all:
#     print(row)


# 新增資料
cursor.execute('insert into account(account,password) values (23423,12312)')
print("添加成功")
# cursor.execute('insert into account(name) values ("花茶")')

# 取得所有数据库数据
cursor.execute('SELECT * FROM account')

# 關閉資料庫連線
db.close()
# # 檢視資料庫資料
# data = cursor.execute('select *from product; ')
# com.commit()  # =>執行
# print("%s顯示成功", (data))
# 關閉資料庫連線
# com.close()
