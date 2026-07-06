import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (count INTEGER);")
    cur.execute("SELECT count FROM visits;")
    row = cur.fetchone()
    if row is None:
        count = 1
        cur.execute("INSERT INTO visits (count) VALUES (%s);", (count,))
    else:
        count = row[0] + 1
        cur.execute("UPDATE visits SET count = %s;", (count,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Hello from the API", "visits": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
