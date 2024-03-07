專案目的-製作登入流程
V1(第一版)
01.main.html使用表單欄位(form)
02.使用fun.js使用ajax傳送資料到flask
03.使用flask架設aplicaton sever接收資料
04.接api收到的資料丟到sql裡

<h2>===完成進度===
<h4>112.3.8-進度(1~3)

<h4>碰到問題-
Q1.flask-route預設為get

```python
@app.route('/register', methods=['POST'])
def register():
```

<h4>Q2.跨域問題(開白名單跟安裝套件)

安裝跨域套件
```python
pip install flask-cors
```

開白名單
```sql
flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5501'])
```
