#from http.server import BaseHTTPRequestHandler

#class handler(BaseHTTPRequestHandler):
 #   def do_GET(self):
   #     self.send_response(200)
   #     self.send_header('Content-type', 'text/plain')
   #     self.end_headers()
    #    self.wfile.write('Hello from Vercel Serverless Python in index page!'.encode('utf-8'))
    #    return##
from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def home():
    return "這是 Flask 的首頁 API"

@app.route('/api/hello')
def say_hello():
    # 自動幫你抓參數，不用再辛苦 parse URL
    name = request.args.get('name', '陌生人')
    return f"嗨 {name}，這是用 Flask 寫的微服務！"

# 這行很重要，讓 Vercel 能抓到 app 對象
if __name__ == "__main__":
    app.run()
