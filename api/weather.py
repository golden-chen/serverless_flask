import requests
from flask import Flask, jsonify

# 注意：如果是在 Vercel 的獨立檔案，建議還是用 Flask 處理會方便很多
app = Flask(__name__)

@app.route('/api/weather')
def get_weather():
    try:
        # 1. 呼叫外部的氣象服務 (wttr.in) 抓取台北的天氣，格式設定為 JSON
        # ?format=j1 是 wttr.in 的 JSON 格式參數
        response = requests.get("https://wttr.in/Taipei?format=j1")
        data = response.json()
        
        # 2. 從複雜的資料中提取我們要的：當前氣溫與天氣描述
        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['weatherDesc'][0]['value']
        
        return {
            "city": "台北",
            "temperature": f"{temp}°C",
            "description": desc,
            "source": "wttr.in"
        }
    except Exception as e:
        return {"error": str(e)}, 500

# 為了讓 Vercel 識別這個檔案的進入點
def handler(request):
    return app(request)
