import sqlite3

DB_PATH = 'database.sqlite'

def connect_db(db_path=DB_PATH):
    """Vytvoří a vrátí připojení k SQLite databázi

    Args:
        db_path (str): Cesta k databázovému souboru. Výchozí hodnota je DB_PATH

    Returns:
        sqlite3.Connection: Objekt připojení k databázi nebo None při chybě
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error:
        print("Nepodařilo se připojit k databázi")
        return None


def create_db():
    """Vytvoří novou databázi podle SQL skriptu

    Načte SQL příkazy ze souboru 'scheme.sql' a provede je
    pro vytvoření databázové struktury.
    """
    conn = connect_db()
    if conn is None:
        return

    script = "scheme.sql"
    try:
        with open(script, 'r') as file:
            conn.executescript(file.read())
    except FileNotFoundError:
        print(f"Soubor {script} nebyl nalezen")
    except sqlite3.Error as e:
        print(f"Chyba při vytváření databáze: {e}")
    finally:
        conn.close()


def db_execute(command, params=False, path=DB_PATH):
    """Provede SQL příkaz v databázi a vrátí výsledky

    Args:
        command (str): SQL příkaz k provedení
        params (tuple/list/dict, optional): Parametry pro parametrizovaný dotaz
        path (str, optional): Cesta k databázovému souboru

    Returns:
        list: Seznam řádků výsledků dotazu nebo prázdný seznam při chybě
    """
    conn = connect_db(path)
    if conn is None:
        return []

    try:
        if params:
            result = conn.execute(command, params).fetchall()
        else:
            result = conn.execute(command).fetchall()
        conn.commit()
        return result
    except sqlite3.Error as e:
        print(f"Chyba při provádění dotazu: {e}")
        return []
    finally:
        conn.close()