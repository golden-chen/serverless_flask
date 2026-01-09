from flask import Flask, jsonify, request
from api.weather import get_taipei_weather # 匯入剛才寫的功能

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
def say_hello1():
    name = request.args.get('name', 'golden')
    return f"嗨 {name}，這是在 Vercel 123 test 回傳的！"
@app.route('/api/add')
@app.route('/add')
def add_numbers():
    # 接收前端傳來的 a 和 b
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    result = a + b
    return f"計算結果：{a} + {b} = {result}"  
@app.route('/api/weather')
def weather_api():
    try:
        data = get_taipei_weather()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500    
if __name__ == "__main__":
    app.run()
