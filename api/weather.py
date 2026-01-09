import requests
from flask import Flask, jsonify

app = Flask(__name__)

# 注意：這裡的路由要對應檔案名稱，或者用萬用匹配
@app.route('/api/weather')
def get_weather():
    try:
        # 抓取氣象資料
        response = requests.get("https://wttr.in/Taipei?format=j1")
        # 檢查外部 API 是否成功
        if response.status_code != 200:
            return jsonify({"error": "外部 API 暫時無法連線"}), 503
            
        data = response.json()
        
        # 提取資料
        current = data['current_condition'][0]
        result = {
            "city": "台北",
            "temperature": f"{current['temp_C']}°C",
            "description": current['weatherDesc'][0]['value'],
            "humidity": f"{current['humidity']}%"
        }
        
        # 強制以 JSON 格式回傳
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 這行是關鍵：讓 Vercel 啟動 Flask
def handler(request):
    return app(request)
