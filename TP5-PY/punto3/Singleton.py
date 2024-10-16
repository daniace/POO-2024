import psycopg2

class SingletonDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
        return cls._instance

    def __init__(self, dsn):
        if not hasattr(self, '_pool'):
            try:
                self._pool = psycopg2.pool.SimpleConnectionPool(1, 10, dsn=dsn)
            except Exception as error:
                print(f"Error connecting to PostgreSQL: {error}")
    
    def get_connection(self):
        return self._pool.getconn()

    def release_connection(self, conn):
        self._pool.putconn(conn)

    def close_all(self):
        self._pool.closeall()

# Uso del SingletonDB para PostgreSQL
if __name__ == "__main__":
    dsn = "dbname=test user=postgres password=secret host=localhost port=5432"
    db_instance = SingletonDB(dsn)
    
    conn = db_instance.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print(cursor.fetchone())
    
    db_instance.release_connection(conn)
    db_instance.close_all()