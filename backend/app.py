from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db  # 引用資料庫配置文件

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5501'])
users = []
cursor = db.cursor()


@app.route('/')
def hello_world():
    return 'Hello, World!'

# data = request.json  # 假設前端使用 JSON 格式傳遞資料
# flask預設方式為get


@app.route('/register', methods=['POST'])
def register():
    # 從 data 中取得需要的資料
    account = request.form.get('username')
    password = request.form.get('password')
    # 在這裡處理註冊邏輯，這僅是一個範例
    # 假設你有一個名為 users 的列表來保存用戶資料
    # 將資料寫入 MySQL 資料庫
    query = "INSERT INTO account (account, password) VALUES (%s, %s)"
    values = (account, password)

    cursor.execute(query, values)
    db.commit()

    return jsonify({'message': 'Registration successful'})


if __name__ == '__main__':
    app.run(debug=True)
