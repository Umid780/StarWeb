from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = 'db.sqlite3'  # Django bilan bir xil SQLite ishga tushgayincha demo

def query_db(q):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = "SELECT id, brand, model, year, price FROM cars_car WHERE LOWER(brand) LIKE ? OR LOWER(model) LIKE ? LIMIT 50"
    term = f"%{q.lower()}%"
    cur.execute(sql, (term, term))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.route('/search')
def search():
    q = request.args.get('q','')
    if not q:
        return jsonify([])
    results = query_db(q)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)