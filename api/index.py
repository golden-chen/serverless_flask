from flask import Flask, request

app = Flask(__name__)

# 1. 處理 /api
@app.route('/api')
def home():
    return "Flask API 運作中！"

# 2. 處理 /api/hello
@app.route('/api/hello')
def say_hello():
    name = request.args.get('name', '陌生人')
    return f"嗨 {name}，這是 Flask 路由回應的！"

# 3. 萬用路由 (除錯用)
@app.route('/api/<path:path>')
def catch_all(path):
    return f"你訪問了 /api/{path}，但 Flask 沒定義這個路徑。"
