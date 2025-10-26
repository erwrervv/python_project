from flask import Flask,render_template,jsonify,Response
import json
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import pandas as pd

app = Flask(__name__)
# 讓app輸出json時,繁體中文不會出現亂碼
# 必須放在 jsonify 之前設定
app.config['JSON_AS_ASCII'] = False
# 讓app輸出json時,繁體中文不會出現亂碼,支援新的flask版本
app.config['JSON_SORT_KEYS'] = False  # 可選，防止自動排序 key
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Run development server. Use a production WSGI server in production.
    app.run(host="127.0.0.1", port=5000, debug=True)
