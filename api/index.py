from flask import Flask, request

app = Flask(__name__)

# 支援訪問 /api 和 /api/
@app.route('/api')
@app.route('/api/')
def home():
    return "Flask 伺服器已啟動！"

# 同時支援有 /api 和 沒有 /api 的路由
@app.route('/api/hello')
@app.route('/hello')
def say_hello():
    name = request.args.get('name', '朋友')
    return f"嗨 {name}，這是在 Vercel 運行的 Flask 回傳的！"
@app.route('/api/test/123')
@app.route('/test/123')
def say_hello():
    name = request.args.get('name', 'golden')
    return f"嗨 {name}，這是在 Vercel 123 test 回傳的！"
if __name__ == "__main__":
    app.run()
