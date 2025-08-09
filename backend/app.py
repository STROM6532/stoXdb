from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from database import get_db_connection
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend testing

# ---------- FRONTEND ROUTES ----------
@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------- API ROUTES ----------
@app.route("/api/companies")
def get_companies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, symbol, name, sector FROM companies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route("/api/stocks")
def get_stocks():
    symbol = request.args.get("symbol")
    from_date = request.args.get("from")
    to_date = request.args.get("to")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT sp.date, sp.open, sp.high, sp.low, sp.close, sp.volume
        FROM stock_prices sp
        JOIN companies c ON sp.company_id = c.id
        WHERE c.symbol = %s
    """
    params = [symbol]

    if from_date:
        query += " AND sp.date >= %s"
        params.append(from_date)
    if to_date:
        query += " AND sp.date <= %s"
        params.append(to_date)

    query += " ORDER BY sp.date ASC"

    cursor.execute(query, tuple(params))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
