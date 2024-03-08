# app.py原始檔案
# 進度 1.跨域 2.順利接收資料
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5501'])
users = []


@app.route('/')
def hello_world():
    return 'Hello, World!'


# flask預設方式為get
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    # 在這裡處理註冊邏輯，這僅是一個範例
    # 假設你有一個名為 users 的列表來保存用戶資料
    users.append({'username': username, 'password': password})
    print(users)
    return jsonify({'message': 'Registration successful'})


if __name__ == '__main__':
    app.run(debug=True)
