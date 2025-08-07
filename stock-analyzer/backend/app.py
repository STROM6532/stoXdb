from flask import Flask, render_template, request, jsonify
from database import get_stock_data
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    company = request.form['company']
    data = get_stock_data(company)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
