import sqlite3
DB_PATH = 'database.sqlite'
def connect_db(db_path = DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.SQLITE_ERROR:
        print("Nepodařilo se připojit k databázi")

def create_db():
    conn = connect_db()
    script = "scheme.sql"
    with open(script, 'r') as file:
        conn.executescript(file.read())
    conn.close()

def db_execute(command, path=DB_PATH):
    conn = connect_db(path)
    cursor = conn.execute(command)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


