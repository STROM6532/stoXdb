from flask import Flask, render_template, request, jsonify
from database import get_connection, get_stock_data
from fetch_data import fetch_and_store_latest_data

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend/pages')


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    symbol = request.args.get('symbol', 'AAPL')
    data = get_stock_data(symbol)
    return jsonify(data)


@app.route('/api/update', methods=['POST'])
def update_data():
    fetch_and_store_latest_data()
    return jsonify({"message": "Data updated successfully"})


if __name__ == '__main__':
    app.run(debug=True)
