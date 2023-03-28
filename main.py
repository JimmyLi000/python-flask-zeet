# 引入必要的套件
from flask import Flask, request, abort

# 建立 Flask 應用程式物件
app = Flask(__name__)

@app.route("/")     # 函式的裝飾 , /是要處理的路徑
def hello_world():  #定義一個fucntion叫hello_world()
    html = f"<h1>Deployed with Zeet!!</h1>"
    return html

if __name__ == '__main__':      # 如果執行主程式
	app.run(host="0.0.0.0", port=3000)   # 立刻啟動伺服器
